from fastapi import APIRouter
from routers.user.api import user_router


api_router = APIRouter()
api_router.include_router(user_router, prefix='/user', tags=['user'])

