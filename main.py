from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from flask import Flask
from asgiref.wsgi import WsgiToAsgi
import uvicorn
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session  # Importer Session ici
from pydantic import BaseModel
from datetime import datetime
from typing import List

# Créer une app Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def home_flask():
    return "<h1>Bonjour depuis Flask</h1>"

# Convertir Flask en ASGI pour FastAPI
asgi_flask_app = WsgiToAsgi(flask_app)

# Créer une app FastAPI
app = FastAPI()

# Monter le dossier static pour servir les fichiers CSS et JS
app.mount("/static", StaticFiles(directory="static"), name="static")

# Monter Flask sous /flask
app.mount("/flask", asgi_flask_app)

# Configuration de la base de données avec SQLAlchemy
DATABASE_URL = "sqlite:///./test.db"  # Utiliser SQLite pour la simplicité
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modèle Article pour SQLAlchemy
class ArticleDB(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    author = Column(String)
    date_published = Column(DateTime, default=datetime.utcnow)

# Créer les tables dans la base de données
Base.metadata.create_all(bind=engine)

# Modèle Pydantic pour la validation des données
class Article(BaseModel):
    title: str
    content: str
    author: str
    date_published: datetime

# Fonction pour obtenir une session de base de données
def get_db():
    db = SessionLocal()  # Créer la session
    try:
        yield db
    finally:
        db.close()  # Fermer la session après utilisation

# Route principale FastAPI
@app.get("/", response_class=HTMLResponse)
async def home_fastapi():
    return """
    <html>
        <head><title>Bienvenue sur FastAPI</title></head>
        <body>
            <h1>Bonjour depuis FastAPI !</h1>
            <p>Page de contenu HTML avec du style CSS intégré.</p>
        </body>
    </html>
    """

# Route pour afficher la liste des articles
@app.get("/articles/", response_class=HTMLResponse)
async def read_articles(db: Session = Depends(get_db)):  # Correctement utiliser Session ici
    articles = db.query(ArticleDB).all()  # Interroger la base de données
    article_list_html = ""
    for article in articles:
        article_list_html += f"""
            <div>
                <h3>{article.title}</h3>
                <p>{article.content}</p>
                <small><i>Par {article.author} le {article.date_published}</i></small>
                <hr>
            </div>
        """
    return f"""
    <html>
        <head><title>Liste des Articles</title></head>
        <body>
            <h1>Articles</h1>
            {article_list_html}
        </body>
    </html>
    """

# Route pour afficher le formulaire d'ajout d'article
@app.get("/ajouter_article/", response_class=HTMLResponse)
async def ajouter_article():
    return """
    <html>
        <head><title>Ajouter un Article</title></head>
        <body>
            <h1>Ajouter un Nouvel Article</h1>
            <form action="/articles/" method="post">
                <label for="title">Titre:</label><br>
                <input type="text" id="title" name="title" required><br><br>
                
                <label for="content">Contenu:</label><br>
                <textarea id="content" name="content" required></textarea><br><br>

                <label for="author">Auteur:</label><br>
                <input type="text" id="author" name="author" required><br><br>

                <label for="date_published">Date de publication:</label><br>
                <input type="datetime-local" id="date_published" name="date_published" required><br><br>

                <button type="submit">Publier l'Article</button>
            </form>
        </body>
    </html>
    """

# Route pour publier un article
@app.post("/articles/")
async def create_article(article: Article, db: Session = Depends(get_db)):  # Correctement utiliser Session ici
    db_article = ArticleDB(
        title=article.title,
        content=article.content,
        author=article.author,
        date_published=article.date_published
    )
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return f"""
    <html>
        <head><title>Article Publié</title></head>
        <body>
            <h1>Article Publié !</h1>
            <p><strong>{article.title}</strong> a été publié par {article.author} le {article.date_published}.</p>
            <a href="/articles/">Voir tous les articles</a>
        </body>
    </html>
    """

# Lancer l'application avec `python main.py`
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
