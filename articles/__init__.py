from flask import Blueprint

# Crée un blueprint pour gérer les articles
articles_bp = Blueprint('articles', __name__)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialiser l'application Flask
app = Flask(__name__)

# Configurer la base de données (ici, SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ta_base.db'  # Le fichier .db sera dans le même dossier que ton script
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialiser SQLAlchemy
db = SQLAlchemy(app)

# Importer les modèles après avoir initialisé db (évite un problème d'importation circulaire)
from articles.models import Article  # Importer ton modèle Article

