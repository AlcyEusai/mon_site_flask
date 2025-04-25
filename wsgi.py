from flask import Flask
import threading
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
    flask_app.run(host="0.0.0.0", port=5000)

# Fonction pour démarrer FastAPI avec uvicorn
def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=10000)

if __name__ == "__main__":
    # Démarre Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Démarre FastAPI
    run_fastapi()

    flask_thread.join()
