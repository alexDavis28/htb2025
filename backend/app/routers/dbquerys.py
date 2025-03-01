from fastapi import HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from fastapi import status

from ..services.logs import log
from ..main import app, db, UID_validate

@app.get("/api/login/{username}")
async def login(username: str, response: Response):
    log.debug("Login", f"Logging in {username}")
    user_id = db.get_user_id(username)
    if user_id is None: raise HTTPException(status_code=404, detail="User not found")
    response.set_cookie(key="UID", value=str(user_id))
    return RedirectResponse(url="/filelist", status_code=status.HTTP_302_FOUND)

@app.get("/api/logout")
async def logout(response: Response):
    response.delete_cookie("UID")
    return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

@app.get("/api/filelist")
async def filelist(request: Request, response: Response):
    UID = UID_validate(request, response)
    if UID is None: 
        log.debug("FileList", "Invalid UID")
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

    log.debug("FileList", f"Getting file list for {UID}")

    file_list = db.get_user_files(str(UID))
    return {"files": file_list}