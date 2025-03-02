from fastapi import Response, Request, APIRouter


from .validation import UID_validate, db, filestore # type: ignore
from ..services.logs import log


router = APIRouter(
    prefix="/analysis",
    tags=["analysis"],

    responses={404: {"description": "Not found"}},
)


@router.post("/green_percent/{file_hash}") 
def green_percent(request: Request, response: Response):
    log.debug("Analysis", f"Green percent request {request}")
    log.debug("Analysis", f"Green percent response {response}")
    return {"green_percent": 0.5}