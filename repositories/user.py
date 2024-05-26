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
    async def new_user(self, username: str, password: str):
        raise NotImplementedError()
    
    @abstractmethod
    async def get_all(self) -> list[User]:
        raise NotImplementedError()
    
    @abstractmethod
    async def get_by_id(self, id: int) -> User:
        raise NotImplementedError()
    

    @abstractmethod
    async def get_by_username(self, username: str) -> User:
        raise NotImplementedError()
    
################################################################################################################################
################################################################################################################################
## Adapter
################################################################################################################################
################################################################################################################################

class __UserRepositoryDB(UserRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
    
    async def new_user(self, username: str, password: str):
        create_new_user = User(
            username=username,
            hashpassword=password,
        )
        with self.session as db:
            db.add(create_new_user)
            db.commit()
            db.refresh(create_new_user)

    async def get_all(self) -> list[User]:
        with self.session as db:
            data = db.query(User).all()
        return data
    
    async def get_by_id(self, id: int) -> User:
        with self.session as db:
            data = db.query(User).filter(User.userid == id).first()
        return data
    
    async def get_by_username(self, username: str) -> User:
        with self.session as db:
            user = db.query(User).filter(User.username == username).first()
        return user

def NewUserRepositoryDB(db: Session) -> UserRepository:
    Base.metadata.create_all(bind=engine)
    return __UserRepositoryDB(session=db)

