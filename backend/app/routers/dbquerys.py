from fastapi import Response, Request, APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status

from typing import Dict, Any

from ..services.logs import log
from .validation import db


router = APIRouter(
    prefix="/api",
    tags=["api"],

    responses={404: {"description": "Not found"}},
)


@router.get("/signup/{username}")
async def signup(username: str, response: Response) -> Dict[Any, Any]:
    log.debug("Signup", f"Signing up {username}")

    if db.add_user(username):
        log.debug("Signup", f"User {username} created")
        uid = db.get_user_id(username)
        if uid is None:
            log.critical("Signup", f"User {username} not found")
            return {}
        return {"user_id": uid}
    else:
        log.debug("Signup", f"User {username} already exists")
        return {}


@router.get("/login/{username}")
async def login(username: str, response: Response) -> Dict[Any, Any]:
    log.debug("Login", f"Logging in {username}")
    user_id = db.get_user_id(username)

    if user_id is None:
        log.debug("Login", f"User {username} not found")
        return {}
    
    return {"user_id": user_id}

@router.get("logout")
async def logout(response: Response):
    return RedirectResponse(url="/public/index.html", status_code=status.HTTP_302_FOUND)

@router.get("/filelist/{user_id}")
async def filelist(user_id: str, request: Request, response: Response) -> Dict[Any, Any]:
    username = db.get_user_name(int(user_id))
    if username is None: return {}

    log.debug("FileList", f"Getting file list for {username}")

    file_list = db.get_user_files(user_id)
    return {"files": file_list}