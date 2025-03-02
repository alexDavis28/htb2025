from fastapi import HTTPException, Response, Request, APIRouter
from fastapi.responses import RedirectResponse
from fastapi import status
from pydantic import BaseModel

from base64 import urlsafe_b64decode, urlsafe_b64encode

from .validation import UID_validate, db, filestore
from ..services.logs import log


router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],

    responses={404: {"description": "Not found"}},
)


@router.post("/green_percent/{file_hash}") 
def green_percent(request: Request, response: Response):
    UID = UID_validate(request, response)
    if UID is None: 
        log.debug("GreenPercent", "Invalid UID")
        return RedirectResponse(url="/public/index.html", status_code=status.HTTP_302_FOUND)

    