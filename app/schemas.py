from pydantic import BaseModel

class User(BaseModel):
    id:int
    username:str
    nombre:str
    rol:str
    estado:int

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    nombre:str

    class Config:
        orm_mode = True

class Respuesta(BaseModel):
    mensaje:str