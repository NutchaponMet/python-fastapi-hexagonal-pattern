from pydantic import (
    BaseModel,
    Field
)

class UserReq(BaseModel):
    username: str
    password: str