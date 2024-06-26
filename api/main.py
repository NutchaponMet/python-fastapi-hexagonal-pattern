from fastapi import APIRouter
from api.routers import user, auth

root = APIRouter()

##############################################################################################################################
## User Router ##
##############################################################################################################################
root.include_router(user.router, prefix="/user", tags=["User API"])
##############################################################################################################################
## Auth Router ##
##############################################################################################################################
root.include_router(auth.router, prefix="/auth", tags=["Authentication"])