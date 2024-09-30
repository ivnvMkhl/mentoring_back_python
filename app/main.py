from fastapi import Depends, FastAPI
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
from app.config import settings
from operator import attrgetter

MAIN_API_PREFIX = attrgetter('MAIN_API_PREFIX')(settings)

app = FastAPI(
    title="mentors_web_app",
    docs_url=f"{MAIN_API_PREFIX}/docs",
    openapi_url=f"{MAIN_API_PREFIX}/openapi.json"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix=f"{MAIN_API_PREFIX}/auth/jwt",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix=f"{MAIN_API_PREFIX}/auth",
    tags=["auth"],
)
app.include_router(lesson_router, prefix=MAIN_API_PREFIX)
app.include_router(menti_router, prefix=MAIN_API_PREFIX)
app.include_router(user_router, prefix=MAIN_API_PREFIX)


current_user = fastapi_users.current_user()
current_active_user = fastapi_users.current_user(active=True)

@app.get(f"{MAIN_API_PREFIX}/protected-route")
def protected_route(user: User = Depends(current_active_user)):
    return f"Hello, {user.user_name}"

@app.get(f"{MAIN_API_PREFIX}/upprotected-route")
def unprotected_route(user: User = Depends(current_user)):
    return f"Hello, anonymus"

#Запуск сервера uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True)