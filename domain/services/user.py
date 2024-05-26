################################################################################################################################
## Import Library
################################################################################################################################

from abc import (
    ABC,
    abstractmethod
)
from repositories import user

################################################################################################################################
################################################################################################################################
## Interface | Port
################################################################################################################################
################################################################################################################################

class UserService(ABC):
    @abstractmethod
    async def get_users(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def get_user_by_id(self, id: int):
        raise NotImplementedError()

################################################################################################################################
################################################################################################################################
## Adapter
################################################################################################################################
################################################################################################################################

class __Userservice(UserService):
    def __init__(self, userRepo: user.UserRepository) -> None:
        self.userRepo = userRepo
    
    async def get_users(self):
        data = await self.userRepo.get_all()
        return data
    
    async def get_user_by_id(self, id: int):
        data = await self.userRepo.get_by_id(id)
        return data

def NewUerService(userRepo: user.UserRepository) -> UserService:
    return __Userservice(userRepo)