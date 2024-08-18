from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, str_uniq, int_pk, str_null_true, def_false
from datetime import datetime
#from app.lesson.models import Lesson

class Menti(Base):
    id : Mapped[int_pk]
    user_id : Mapped[int]
    name : Mapped[str]
    last_name : Mapped[str]
    email : Mapped[str_uniq]
    phone : Mapped[str_uniq]
    telegram : Mapped[str_uniq]
    city : Mapped[str]
    grade : Mapped[str]
    education : Mapped[str]
    is_delete : Mapped[bool] = mapped_column(server_default=text("false"))


    #Отношения
    lessons: Mapped[list["Lesson"]] = relationship("Lesson", back_populates='menti')
    extend_existing = True

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id})"

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id" : self.id,
            "user_id" : self.user_id,
            "name" : self.name,
            "last_name" : self.last_name,
            "email" : self.email,
            "phone" : self.phone,
            "telegram" : self.telegram,
            "city" : self.city,
            "grade" : self.grade,
            "education" : self.education,
        }
