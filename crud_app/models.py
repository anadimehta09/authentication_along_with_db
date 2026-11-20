from sqlalchemy import String, Column, Integer
from crud_app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id= Column(Integer , primary_key=True, index=True)
    name= Column(String, index= True)
    email= Column(String, unique=True, index=True)
    hashed_password = Column(String)