from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, func, text, Text, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base, str_uniq, int_pk, str_null_true, def_false,created_at
from datetime import datetime, tzinfo, date, time

class Lesson(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int]
    menti_id: Mapped[int] = mapped_column(ForeignKey("mentis.id"), nullable=False)
    donate: Mapped[int]
    lesson_date: Mapped[date]
    lesson_time: Mapped[time]
    canceled: Mapped[bool] = mapped_column(server_default=text("false"))
    is_delete: Mapped[bool] = mapped_column(server_default=text("false"))

    # Определяем отношения: один урок - один ментор и один ученик
    menti: Mapped["Menti"] = relationship("Menti", back_populates="lessons")
    extend_existing = True


    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"user_id={self.user_id!r},"
                f"menti_id={self.menti_id!r},"
                f"date_of_lesson={self.lesson_date!r},"
                f"time_of_lesson={self.lesson_time!r}")

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "menti_id": self.menti_id,
            "donate": self.donate,
            "lesson_date": self.lesson_date,
            "lesson_time": self.lesson_time,
            "canceled": self.canceled,
            "is_delete": self.is_delete,
        }