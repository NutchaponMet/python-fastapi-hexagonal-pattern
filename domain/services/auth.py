from abc import (
    ABC,
    abstractmethod
)
from datetime import datetime, timedelta
from jose import jwt
import bcrypt
from domain.core.config import settings
from repositories import user
from domain.schemas.token import Token

################################################################################################################################
################################################################################################################################
## Interface | Port
################################################################################################################################
################################################################################################################################

class AuthenticationService(ABC):
    @abstractmethod
    async def authenticate_user(self, username: str, password: str,) -> Token:
        raise NotImplementedError()
    
    @abstractmethod
    async def create_user(self, username: str, password: str) -> str:
        raise NotImplementedError()

################################################################################################################################
################################################################################################################################
## Adapter
################################################################################################################################
################################################################################################################################

class __AuthenticationService(AuthenticationService):
    def __init__(self, userRepo: user.UserRepository) -> None:
        self.userRepo = userRepo

    async def authenticate_user(self, username: str, password: str) -> Token:
        user = await self.userRepo.get_by_username(username)
        if not user:
            return False
        if not bcrypt.checkpw(password.encode(), user.hashpassword.encode()):
            return False
        token = self.__create_access_token(user.username, user.userid, timedelta(minutes=30))
        return Token(
            access_token=token,
            token_type="bearer"
        )
    
    async def create_user(self, username: str, password: str) -> str:
        salt = bcrypt.gensalt()
        hashpwd = bcrypt.hashpw(password.encode(), salt=salt).decode()
        await self.userRepo.new_user(
            username=username,
            password=hashpwd
        )
        return "Created"
    
    def __create_access_token(self, username: str, user_id: int, expires_delta:timedelta):
        encode = {'sub':username, 'id':user_id}
        expires = datetime.now() + expires_delta
        encode.update({'exp': expires})
        return jwt.encode(encode, settings.SECRET_KEY,algorithm=settings.ALGORITHM)
    

def NewAuthenticationService(userRepo: user.UserRepository) -> AuthenticationService:
    return __AuthenticationService(userRepo)