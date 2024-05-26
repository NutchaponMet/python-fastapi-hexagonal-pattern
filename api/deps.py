from typing import Annotated
from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session
from domain.core.db import get_db
from fastapi.security import OAuth2PasswordBearer
from domain.core.config import settings
from jose import jwt, JWTError

db_dependency = Annotated[Session, Depends(get_db)]



oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail='Could not validate user.')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Could not validate user.')

user_dependency = Annotated[dict, Depends(get_current_user)]