from abc import (
    ABC,
    abstractmethod
)
from datetime import datetime, timedelta
import bcrypt
from repositories import user
from domain.schemas.token import Token
from domain import util


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
        if not util.verify(password, user.hashpassword):
            return False
        token = util.create_access_token(user.username, user.userid, timedelta(minutes=30))
        return Token(
            access_token=token,
            token_type="bearer"
        )
    
    async def create_user(self, username: str, password: str) -> str:
        hashpwd = util.hash_password(password)
        await self.userRepo.new_user(
            username=username,
            password=hashpwd
        )
        return "Created"
    

def NewAuthenticationService(userRepo: user.UserRepository) -> AuthenticationService:
    return __AuthenticationService(userRepo)