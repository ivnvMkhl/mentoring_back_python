
from datetime import datetime, date, time


class RBLesson:
    def __init__(self, lesson_id: int | None = None,
                 user_id: int | None = None,
                 menti_id: int | None = None,
                 lesson_date: date| None = None,
                 lesson_time: time | None = None,
                 donate: int | None = None,
                 canceled: bool | None =None):
        self.id = lesson_id
        self.user_id = user_id
        self.menti_id = menti_id
        self.lesson_date = lesson_date
        self.lesson_time = lesson_time
        self.donate = donate
        self.canceled = canceled
       
    def to_dict(self) -> dict:
        data = {'id': self.id, 'user_id': self.user_id, 'menti_id': self.menti_id, 'lesson_date': self.lesson_date,
                'lesson_time': self.lesson_time,'donate' : self.donate, 'canceled': self.canceled}
        #Создаем копию словаря чтобы избежать его изменения во время итерации
        filtred_data = {key:value for key,value in data.items() if value is not None}
        return filtred_data