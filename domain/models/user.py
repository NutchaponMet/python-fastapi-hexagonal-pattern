from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer
from domain.core.db import Base

class User(Base):
    __tablename__ = "user"
    userid = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String)
    hashpassword = mapped_column(String)