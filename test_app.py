# flask_app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

@app.route('/call_fastapi')
def call_fastapi():
    response = requests.get("http://localhost:10000/fastapi")
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, port=5000)
