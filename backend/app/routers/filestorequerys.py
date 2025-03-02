from fastapi import Response, UploadFile, APIRouter
from pydantic import BaseModel

from typing import Dict, Any

from base64 import urlsafe_b64encode

from .validation import db, filestore
from ..services.logs import log


router = APIRouter(
    prefix="/store",
    tags=["store"],

    responses={404: {"description": "Not found"}},
)


@router.get("/{item_hash}")
async def read_item(item_hash: str) -> Dict[Any, Any]:
    log.debug("Store", f"Getting file {item_hash}")
    file_data = filestore.get_file(item_hash)
    if file_data is None: return {}
    return {"data": urlsafe_b64encode(file_data).decode()}

class UploadData(BaseModel):
    name: str
    data: str


@router.post("/upload/{user_id}")
async def create_upload(user_id:str, file: UploadFile, response: Response) -> Dict[Any, Any]:
    if file.filename is None: return {}

    username = db.get_user_name(int(user_id))
    if username is None:
        log.debug("Upload", f"User {user_id} not found")
        return {}

    raw = file.file.read()
    
    # File save 
    success, file_hash = filestore.save_file(raw)
    if file_hash is None: 
        log.debug("Upload", "Failed to save file")
        return {}
    
    # validate savev
    if success:
        if not db.add_file_record(file.filename, file_hash):
            log.critical("Upload", "Failed to add file record")
            return {}
        log.debug("Upload", f"Added file record {file.filename}")
    else:
        log.debug("Upload", f"File '{file.filename}' already exists")
    
    # get generated FID
    FID = db.get_file_id(file_hash)
    if FID is None:
        log.critical("Upload", f"Failed to get file_id of uploaded file {file_hash}")
        return {}

    # Add file to user
    if not db.add_user_file(int(user_id), FID):
        log.critical("Upload", f"Failed to add file {file_hash} to user {user_id}")
        return {}


    return {"file_hash": file_hash}