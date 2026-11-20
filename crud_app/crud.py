from sqlalchemy.orm import Session
from pwdlib import PasswordHash
from crud_app import models, schemas


password_hash = PasswordHash.recommended()

def get_employee(db:Session):
    return db.query(models.Employee).all()

def get_single_employee(db:Session , emp_id:int):
    return db.query(models.Employee).filter(models.Employee.id == emp_id).first()

def create_employee(db:Session,employee:schemas.EmployeeCreate):
    exsisting_email = db.query(models.Employee).filter(models.Employee.email==employee.email).first()
    if exsisting_email:
        print("already exsist")
    
    db_employee = models.Employee(name= employee.name, email=employee.email)
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def update_employee(db:Session, emp_id:int , employee:schemas.EmployeeUpdate):
    db_employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    if db_employee:
        db_employee.name = employee.name
        db_employee.email= employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee
        


def delete_employee(db:Session, emp_id:int,):
    db_employee = db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

def register_user(db:Session,employee:schemas.UserRegister):
    existing_email=db.query(models.Employee).filter(models.Employee.email==employee.email).first()
    if existing_email:
        print("already Registerd")
    hash_password = password_hash.hash(employee.password)
    db_employee=models.Employee(name=employee.username, email=employee.email ,hashed_password=hash_password )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def login_user(db:Session,employee:schemas.UserLogin):
    employee_db= db.query(models.Employee).filter(models.Employee.email==employee.email).first()
    if not employee_db:
        return None
    is_valid = password_hash.verify(employee.password,employee_db.hashed_password)
    if not is_valid:
        return None
    return employee_db
