from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur mon site FastAPI !"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
    from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur mon site Flask !"

if __name__ == '__main__':
    app.run()

