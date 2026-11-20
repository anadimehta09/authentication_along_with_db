from pydantic import BaseModel ,EmailStr

class EmployeeBase(BaseModel):
    name:str
    email:EmailStr

class EmployeeCreate(EmployeeBase):
    pass
class EmployeeUpdate(EmployeeBase):
    pass
class Employeeout(EmployeeBase):
    id:int

    class Config:
        orm_mode=True
class UserRegister(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str