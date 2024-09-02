from fastapi import Depends, FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from redis import asyncio as aioredis

import uvicorn  
from starlette.requests import Request
from starlette.responses import RedirectResponse

import os
import sys


sys.path.append(os.getcwd())

from app.user.models import User
from app.user.schemas import UserCreate, UserRead

from app.lesson.router import router as lesson_router
from app.menti.router import router as menti_router
from app.user.router import router as user_router

from app.user.base_config import auth_backend, fastapi_users
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession


app = FastAPI(
    title="mentors_web_app"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)


app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)




current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)

@app.get("/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.user_name}"



@app.get("/upprotected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, anonymus"

app.include_router(lesson_router)
app.include_router(menti_router)
app.include_router(user_router)


@app.lifespan("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")

#Запуск сервера uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)