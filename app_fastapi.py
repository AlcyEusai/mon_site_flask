from fastapi import FastAPI

fastapi_app = FastAPI()

@fastapi_app.get("/")
async def read_root():
    return {"message": "Hello depuis FastAPI !"}

@fastapi_app.get("/fastapi")
async def fastapi_hello():
    return {"message": "Route FastAPI active"}
