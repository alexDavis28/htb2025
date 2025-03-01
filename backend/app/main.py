from fastapi import FastAPI
from .routers import dbquerys, filestorequerys

app = FastAPI()

app.include_router(dbquerys.router)
app.include_router(filestorequerys.router)

@app.get("/")
async def read_root():
    return {"Hello": "World!"}


