from flask import Flask
import threading
import uvicorn
from app_fastapi import app as fastapi_app  # Importation de FastAPI

# Crée l'application Flask
flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bonjour de Flask !"

# Fonction pour démarrer Flask
def run_flask():
    flask_app.run(host="0.0.0.0", port=5000)

# Fonction pour démarrer FastAPI
def run_fastapi():
    uvicorn.run(fastapi_app, host="127.0.0.1", port=10000)

if __name__ == "__main__":
    # Démarre Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Démarre FastAPI
    run_fastapi()

    flask_thread.join()
