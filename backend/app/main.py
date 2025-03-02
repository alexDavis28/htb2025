from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from .routers import dbquerys, filestorequerys

app = FastAPI()

app.include_router(dbquerys.router)
app.include_router(filestorequerys.router)

@app.get("/")
async def root():
    return RedirectResponse(url="/public/", status_code=301)