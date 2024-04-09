from sqlalchemy import Column, Integer, String, Float
from database import Base

class Employee(Base):
    __tablename__ = 'Employees'
    
    Emp_Id = Column(Integer, primary_key=True, index=True)
    Emp_Name = Column(String, index=True)
    Emp_Age = Column(Integer, index=True)
    position = Column(String,index=True)
    department = Column(String, index=True)
    salary = Column(Float, index=True)
    Contact_number = Column(String, index=True)
    