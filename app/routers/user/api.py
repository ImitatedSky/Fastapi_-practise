from fastapi import APIRouter
from app.routers.user import user , book

user_router = APIRouter()

user_router.include_router(user.router, prefix='/user')
user_router.include_router(book.router, prefix='/book')