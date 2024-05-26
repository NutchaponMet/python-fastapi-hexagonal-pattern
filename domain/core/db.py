from sqlalchemy import create_engine
from sqlalchemy.orm import (
    Session,
    DeclarativeBase,
    sessionmaker
)
from ..core.config import settings

if settings.SERVER_MODE == "release":
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db_container_name/postgres"
else:
    SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin1234@localhost:8080/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)

session = Session(autocommit=False, autoflush=False, bind=engine)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    with sessionLocal() as db:
        yield db