from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'accueil"}

@app.get("/about")
def about():
    return {"message": "Bienvenue sur la page À propos"}
