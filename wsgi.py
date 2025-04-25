import os
import threading
from flask import Flask
import uvicorn
from fastapi import FastAPI

# Crée l'application Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bonjour de Flask !"

# Crée l'application FastAPI
fastapi_app = FastAPI()

@fastapi_app.get("/fastapi")
def fastapi_home():
    return {"message": "Bonjour de FastAPI !"}

# Fonction pour démarrer Flask
def run_flask():
    port = os.environ.get("PORT", 5000)  # Utiliser le port dynamique de Render
    flask_app.run(host="0.0.0.0", port=int(port))

# Fonction pour démarrer FastAPI avec uvicorn
def run_fastapi():
    port = os.environ.get("PORT", 10000)  # Utiliser le port dynamique de Render
    uvicorn.run(fastapi_app, host="0.0.0.0", port=int(port))

if __name__ == "__main__":
    # Démarre Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Démarre FastAPI dans un autre thread
    fastapi_thread = threading.Thread(target=run_fastapi)
    fastapi_thread.start()

    flask_thread.join()
    fastapi_thread.join()
