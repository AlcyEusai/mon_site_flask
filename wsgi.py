from fastapi import FastAPI
from asgiref.wsgi import WsgiToAsgi

from main import flask_app
from app_fastapi import fastapi_app

# Convertir Flask en ASGI
asgi_flask_app = WsgiToAsgi(flask_app)

# Créer l'app principale FastAPI
app = FastAPI()

# Monter Flask et FastAPI ensemble
app.mount("/flask", asgi_flask_app)     # Flask sous /flask
app.mount("/fastapi", fastapi_app)       # FastAPI sous /fastapi

@app.get("/")
async def root():
    return {"message": "Bienvenue sur l'application combinée !"}
