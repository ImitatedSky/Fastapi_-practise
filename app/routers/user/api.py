from fastapi import APIRouter

from app.routers.user import book, user

user_router = APIRouter()

user_router.include_router(user.router, prefix="/user")
user_router.include_router(book.router, prefix="/book")
