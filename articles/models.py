from articles import db  # On importe db depuis __init__.py

# Définition du modèle Article
class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Identifiant unique de l'article
    titre = db.Column(db.String(100))  # Titre de l'article
    contenu = db.Column(db.Text)  # Contenu de l'article
    date_creation = db.Column(db.String(50))  # Date de création

    def __repr__(self):
        return f"<Article {self.titre}>"
