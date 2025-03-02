from fastapi import FastAPI
from .routers import dbquerys, filestorequerys
from fastapi.middleware import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dbquerys.router)
app.include_router(filestorequerys.router)

@app.get("/")
async def root():
    return "Hello world!"
    # return RedirectResponse(url="/public/", status_code=301)