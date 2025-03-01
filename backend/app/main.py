from fastapi import FastAPI
from .conf import config
from .services.logs import Logger

log = Logger()

app = FastAPI()

# app.include_router()

@app.get("/")
def read_root():
    return {"Hello": "World!"}
