from fastapi import (
    APIRouter,
    HTTPException,
    status
)
from domain.core.db import session
from domain.services.user import UerService
from logs.logs import logger
from ..deps import db_dependency

router = APIRouter()

user_service = UerService(session)

@router.get("/test-log")
async def test_log():
    try:
        total = 1.2 + "1.1"
        return {'message': total}
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str("Unexpected server error"))
    
@router.get("/")
async def get_user(db: db_dependency):
    try:
        # resp_data = await UerService(db).get_users()
        resp_data = await user_service.get_users()
        return resp_data
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str("Unexpected server error"))

@router.get("/id")
async def get_by_id(q: int, db: db_dependency):
    try:
        # resp_data = await UerService(db).get_user_by_id(id=q)
        resp_data = await user_service.get_user_by_id(id=q)
        return resp_data
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str("Unexpected server error"))