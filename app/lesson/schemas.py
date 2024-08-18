from datetime import datetime, date, time
from typing import Optional
import re
from pydantic import BaseModel, ConfigDict, Field, EmailStr, field_validator
from sqlalchemy import DateTime

class SLesson(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    user_id: int
    menti_id: int
    donate: int
    lesson_date: date
    lesson_time: time
    canceled: bool

class SLessonADD(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    menti_id: int
    donate: int
    lesson_date: date
    lesson_time: time
    canceled: bool = Field(default=False)


class SLessonUPDATE(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    menti_id: int
    donate: int
    lesson_date: date
    lesson_time: time
    canceled: bool = Field(default=False)


