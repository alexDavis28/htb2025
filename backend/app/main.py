from typing import Optional

from fastapi import FastAPI, Response, Request

from .services.logs import log
from .services.database import DB
from .services.filestore import FileStore


db = DB()
filestore = FileStore()

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World!"}



def UID_validate(request: Request, response: Response) -> Optional[int]:
    log.debug("UID_validate", f"request {request}")
    log.debug("UID_validate", f"cookies {request.cookies}")
    UID = request.cookies.get("UID")
    
    if UID is None:
        return None
    try:
        UID_int:int =  int(UID)
        log.debug("UID_validate", f"UID_int {UID_int}")
        username = db.get_user_name(UID_int)
        log.debug("UID_validate", f"username {username}")
        if username is not None:
            return UID_int
        response.delete_cookie("UID")
        return None           

    except ValueError:
        return None