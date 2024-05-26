from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer
from domain.core.db import Base

class User(Base):
    __tablename__ = "user"
    userid: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String)
    hashpassword: Mapped[str] = mapped_column(String)