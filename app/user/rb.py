class RBUser:
    def __init__(self, 
                 email : str | None = None,
                 user_name : str | None = None,
                 phone : str | None = None,
                 telegram : str | None = None,
                 ):
        self.email = email
        self.user_name = user_name
        self.phone  = phone 
        self.telegram = telegram
       
    def to_dict(self) -> dict:
        data = {'email': self.email,'user_name': self.user_name,'phone' : self.phone, 'telegram': self.telegram}
        #Создаем копию словаря чтобы избежать его изменения во время итерации
        filtred_data = {key:value for key,value in data.items() if value is not None}
        return filtred_data