from fastapi import FastAPI
from conf import config

app = FastAPI()
app.config = config # type: ignore

# app.include_router()

@app.get("/")
def read_root():
    return {"Hello": "World!"}
