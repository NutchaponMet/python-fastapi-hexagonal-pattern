from typing import Annotated
from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends
)
from fastapi.security import (
    OAuth2PasswordRequestForm,
)

from domain.core.db import session
from domain.schemas.user import UserReq
from domain.services.auth import NewAuthenticationService
from repositories.user import NewUserRepositoryDB
from logs.logs import logger

router = APIRouter()

user_repository = NewUserRepositoryDB(session)
auth_service = NewAuthenticationService(user_repository)

@router.post("/registor")
async def registor(new_user: UserReq):
    try:
        resp = await auth_service.create_user(new_user.username, new_user.password)
        if resp == "Created":
            return status.HTTP_201_CREATED
        else:
            raise HTTPException(
                status_code=status.HTTP_304_NOT_MODIFIED, 
                detail=str("Not modified")
            )
    except Exception as e:
        logger.exception(e)
        raise HTTPException(status_code=500, detail=str("Unexpected server error"))
    

@router.post("/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    token = await auth_service.authenticate_user(form_data.username, form_data.password)
    return token