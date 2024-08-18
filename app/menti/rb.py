

class RBMenti:
    def __init__(self, menti_id: int | None = None,
                 user_id: int | None = None,
                 name : str | None = None,
                 last_name: str | None = None,
                 email: str | None = None,
                 phone: str | None = None,
                 telegram: str | None = None,
                 city: str | None = None,
                 grade: str | None = None,
                 education: str | None = None,):
        self.id = menti_id
        self.user_id = user_id
        self.name  = name 
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.telegram = telegram
        self.city = city
        self.grade = grade
        self.education = education
       
    def to_dict(self) -> dict:
        data = {'id': self.id, 'user_id': self.user_id, 'name': self.name, 'last_name': self.last_name,
                'email': self.email,'phone' : self.phone, 'telegram': self.telegram, 'city': self.city, 
                'grade' : self.grade, 'education': self.education}
        #Создаем копию словаря чтобы избежать его изменения во время итерации
        filtred_data = {key:value for key,value in data.items() if value is not None}
        return filtred_data