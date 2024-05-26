from pydantic import (
    BaseModel,
    Field
)

class UserSchema(BaseModel):
    username: str
    password: str
    
class UserResp(UserSchema):
    pass

class UserReq(UserSchema):
    firstname: str
    email: str
    