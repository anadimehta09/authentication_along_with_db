from crud_app import crud, schemas, models
from fastapi import FastAPI , HTTPException , Depends
from sqlalchemy.orm import Session
from crud_app.database import SessionLocal, engine, Base
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_employee",response_model=schemas.Employeeout)
def create_employee(employee:schemas.EmployeeCreate,db:Session=Depends(get_db)):
    return crud.create_employee(db,employee)

@app.get("/read_employee", response_model=schemas.Employeeout)
def read_employee(db:Session = Depends(get_db)):
    return crud.get_employee(db)


# @app.get("/read_employees", response_model=List[schemas.Employeeout])
# def read_employee(db:Session=Depends(get_db)):
#     return crud.get_employee(db)

@app.get("/read_employee/{emp_id}", response_model=schemas.Employeeout)
def read_single_employee(emp_id:int, db:Session=Depends(get_db)):
    employee= crud.get_single_employee(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404 , detail= "employee not found")
    return employee

# @app.get("/read_employee/{emp_id}",response_model=schemas.Employeeout)
# def read_single_employee(emp_id:int , db:Session= Depends(get_db)):
#     employee= crud.get_single_employee(db,emp_id)
#     if employee is None:
#         raise HTTPException(status_code=404 , detail="employee not found")
#     return employee

@app.put("/update_employee/{emp_id}" , response_model=schemas.Employeeout)
def update_employee(emp_id:int , employee:schemas.EmployeeCreate, db:Session= Depends(get_db)):
    employee=crud.update_employee(db,emp_id,employee)
    if employee is None:
        raise HTTPException(status_code=404 , detail="user not found")
    return employee

@app.delete("/delete_employee/{emp_id}", response_model=schemas.Employeeout)
def delete_employee(emp_id:int , db:Session=Depends(get_db)):
    employee = crud.delete_employee(db , emp_id)
    if employee is None :
        raise HTTPException(status_code=404 , detail="user not present")
    return employee

@app.post("/register" ,response_model=schemas.Employeeout)
def register_employee(employee:schemas.UserRegister , db:Session=Depends(get_db)):
    employee = crud.register_user(db,employee)
    if employee is None:
        raise HTTPException(status_code=400,
            detail="Registration failed")
    return employee

@app.post("/login",response_model=schemas.Employeeout)
def login_employee(employee:schemas.UserLogin, db:Session= Depends(get_db)):
    employee=crud.login_user(db,employee)
    if employee is None:
        raise HTTPException(status_code=400 ,detail="unAthorized Access")
    return employee