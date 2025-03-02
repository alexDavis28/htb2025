from fastapi import FastAPI
from .routers import filestorequerys, dbquerys

app = FastAPI()

app.include_router(dbquerys.router)
app.include_router(filestorequerys.router)

@app.get("/")
async def root():
    return "Hello world!"
    # return RedirectResponse(url="/public/", status_code=301)