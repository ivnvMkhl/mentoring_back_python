from pydantic import BaseModel, Field, ConfigDict

class SMenti(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id : int
    user_id : int
    name : str
    last_name : str
    email : str
    phone : str
    telegram : str
    city : str
    grade : str
    education : str
    
class SMentiAdd(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id : int
    name : str
    last_name : str
    email : str
    phone : str
    telegram : str
    city : str
    grade : str
    education : str
