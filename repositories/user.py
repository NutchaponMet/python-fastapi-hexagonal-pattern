################################################################################################################################
## Import Library
################################################################################################################################

from abc import (
    ABC, 
    abstractmethod,
)
from sqlalchemy.orm import Session
from domain.models.user import User
from domain.core.db import (
    Base, 
    engine,
)

################################################################################################################################
################################################################################################################################
## Interface | Port
################################################################################################################################
################################################################################################################################

class UserRepository(ABC):
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError()
    
    @abstractmethod
    async def get_by_id(self, id: int):
        raise NotImplementedError()
    
################################################################################################################################
################################################################################################################################
## Adapter
################################################################################################################################
################################################################################################################################

class __UserRepositoryDB(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
        
    async def get_all(self):
        with self.session as db:
            data = db.query(User).all()
        return data
    
    async def get_by_id(self, id: int):
        with self.session as db:
            data = db.query(User).filter(User.userid == id).first()
        return data

def NewUserRepositoryDB(db: Session) -> UserRepository:
    Base.metadata.create_all(bind=engine)
    return __UserRepositoryDB(session=db)

