from typing import Optional

from fastapi import FastAPI, HTTPException, Response, Request
from fastapi.responses import RedirectResponse
from fastapi import status
from pydantic import BaseModel

from base64 import urlsafe_b64decode, urlsafe_b64encode

from .services.logs import log
from .services.database import DB
from .services.filestore import FileStore



db = DB()
filestore = FileStore()

app = FastAPI()
# app.include_router()

@app.get("/")
async def read_root():
    return {"Hello": "World!"}

@app.get("/store/{item_hash}")
async def read_item(item_hash: str):
    log.debug("Store", f"Getting file {item_hash}")
    file_data = filestore.get_file(item_hash)
    if file_data is None: raise HTTPException(status_code=404, detail="Item not found")
    return {"data": urlsafe_b64encode(file_data).decode()}

class UploadData(BaseModel):
    name: str
    data: str


@app.post("/upload")
async def create_upload(request: Request, response: Response, data: UploadData):
    log.debug("Upload", f"request {request}")
    log.debug("Upload", f"response {response}")
    log.debug("Upload", f"data {data}")



    # UID validation
    UID = UID_validate(request, response)
    if UID is None: 
        log.debug("Upload", "Invalid UID")
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND)

    # File decode
    raw  = urlsafe_b64decode(data.data)
    if raw == b"": 
        log.debug("Upload", "Invalid base64 data")
        raise HTTPException(status_code=400, detail="Invalid base64 data")
    
    # File save 
    success, file_hash = filestore.save_file(raw)
    if file_hash is None: 
        log.debug("Upload", "Failed to save file")
        raise HTTPException(status_code=500, detail="Failed to save file")
    
    # validate savev
    if success:
        if not db.add_file_record(data.name, file_hash):
            log.critical("Upload", "Failed to add file record")
            raise HTTPException(status_code=500, detail="Failed to add file record")
        log.debug("Upload", f"Added file record {data.name}")
    else:
        log.debug("Upload", f"File '{data.name}' already exists")
    
    # get generated FID
    FID = db.get_file_id(file_hash)
    if FID is None:
        log.critical("Upload", f"Failed to get file_id of uploaded file {file_hash}")
        raise HTTPException(status_code=500, detail="Failed to get file_id of uploaded file")

    # Add file to user
    if not db.add_user_file(UID, FID):
        log.critical("Upload", f"Failed to add file {file_hash} to user {UID}")
        raise HTTPException(status_code=500, detail="Failed to add file to user")


    return {"file_hash": file_hash}


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