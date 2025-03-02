from fastapi import Response, Request, APIRouter
from ..services import analysis

from .validation import UID_validate, db, filestore # type: ignore
from ..services.logs import log


router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],

    responses={404: {"description": "Not found"}},
)

@router.post("/process/{file_hash}")
def process_file(file_hash: str):
    log.debug("Analysis", f"{file_hash}")
    a = __import__("base64").b64encode(bytes(file_hash))
    print(a.deocde("utf-8"))
    file_hash = file_hash.strip().replace("\n", "")
    result = analysis.analyse_image(file_hash)
    return {"data": result}