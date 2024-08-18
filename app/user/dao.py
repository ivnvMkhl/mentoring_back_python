
from app.dao.base import BaseDAO
from app.user.models import User


class UserDAO(BaseDAO):
    model = User