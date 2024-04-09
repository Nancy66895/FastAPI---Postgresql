from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from database import get_db
import psycopg2
from models import Employee




app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class CreateEmployee(BaseModel):
    Emp_Id : int
    Emp_Name : str
    Emp_Age : int
    position  :str
    department : str
    salary : float
    Contact_number : str
    
class UpdateEmployee(BaseModel):
    Emp_Id : int
    Emp_Name : str
    Emp_Age : int
    position  :str
    department : str
    salary : float
    Contact_number : str 
    
    
# Create an employee
@app.post("/employee/")
def create_employee(employee: CreateEmployee, db: Session = Depends(get_db)):
    try:
        print(f"employee is {employee.Emp_Name}")
        emp_obj = Employee()
        emp_obj.Emp_Id = employee.Emp_Id
        emp_obj.Emp_Name = employee.Emp_Name
        emp_obj.Emp_Age = employee.Emp_Age
        emp_obj.position = employee.position
        emp_obj.department = employee.department
        emp_obj.salary = employee.salary
        emp_obj.Contact_number = employee.Contact_number
        db.add(emp_obj)
        db.commit()
        db.refresh(emp_obj)
        return {"status": status.HTTP_201_CREATED, "message":"Employee created successfully."}
        
    except Exception as e:
        print(e.__cause__)
        
# Read an employee 
    
@app.get("/employee/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        employee = db.query(CreateEmployee).filter(CreateEmployee.Emp_Id == employee_id).first()
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {
            "Emp_Id": employee.Emp_Id,
            "Emp_Name": employee.Emp_Name,
            "Emp_Age": employee.Emp_Age,
            "position": employee.position,
            "department": employee.department,
            "salary": employee.salary,
            "Contact_number": employee.Contact_number
        }
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Failed to fetch employee")
    
 
# Update an employee
 
@app.put("/Employee_Update")
def update_employee(employee: UpdateEmployee, db: Session = Depends(get_db)):
    try:
        print("In employee update")
       
        db_Employee = db.query(Employee).filter(Employee.Emp_Id == employee.Emp_Id).scalar()
        
        
        if db_Employee.Emp_Id is None:
            raise HTTPException(status_code=404, detail="Employee not found")
        db_Employee = db.query(Employee).filter(Employee.Emp_Id == employee.Emp_Id).scalar()
        print(f"Employee Id is {db_Employee.Emp_Id}")
        
        
        
        db_Employee.Emp_Name = employee.Emp_Name
        db_Employee.Emp_Age = employee.Emp_Age
        db_Employee.position = employee.position
        db_Employee.department = employee.department
        db_Employee.salary = employee.salary
        db_Employee.Contact_number = employee.Contact_number
        
        db.add(db_Employee)
        db.commit()
        
        return {
            "status": status.HTTP_200_OK,
            "message": "Employee updated successfully.",
            "data": {
                "Emp_Id": db_Employee.Emp_Id,
                "Emp_Name": db_Employee.Emp_Name,
                "Emp_Age": db_Employee.Emp_Age,
                "position": db_Employee.position,
                "department": db_Employee.department,
                "salary": db_Employee.salary,
                "Contact_number": db_Employee.Contact_number
            }
        }
        
    except Exception as e:        
        print(e.__cause__)
        
 
# Delete an employee
   
@app.delete("/employee/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    try:
        employee = db.query(Employee).filter(Employee.Emp_Id == employee_id).first()
        
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        
        db.delete(employee)
        db.commit()
        
        return {"status": "Employee deleted successfully"}
        
    except Exception as e:
        print(e.__cause__)
        raise HTTPException(status_code=500, detail="Failed to delete employee")    