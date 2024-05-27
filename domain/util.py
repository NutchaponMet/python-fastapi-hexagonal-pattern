import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from domain.core.config import settings

def hash_password(pwd: str) -> str:
    salt = bcrypt.gensalt()
    hashpwd = bcrypt.hashpw(pwd.encode(), salt=salt).decode()
    return hashpwd

def verify(pwd: str, hash_pwd: str) -> bool:
    return bcrypt.checkpw(pwd.encode(), hash_pwd.encode())

def create_access_token(username: str, user_id: int, expires_delta:timedelta) -> str:
    encode = {'sub':username, 'id':user_id}
    expires = datetime.now() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY,algorithm=settings.ALGORITHM)