# coding: utf-8
# sqlacodegen postgresql://root:root@localhost:25432/root | pbcopy
from sqlalchemy import CheckConstraint, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Department(Base):
    __tablename__ = 'department'

    department_no = Column(Integer, primary_key=True)
    department_name = Column(String(14), unique=True)
    location = Column(String(13))

    employees = relationship('Employee')


class Employee(Base):
    __tablename__ = 'employee'
    __table_args__ = (
        CheckConstraint('salary > 0'),
    )

    employee_no = Column(Integer, primary_key=True)
    employee_name = Column(String(10))
    job = Column(String(9))
    manager_no = Column(Integer)
    hire_date = Column(Date)
    salary = Column(Integer)
    comm = Column(Integer)
    department_no = Column(ForeignKey('department.department_no'))

    department = relationship('Department')


class Jobhist(Base):
    __tablename__ = 'jobhist'
    __table_args__ = (
        CheckConstraint('start_date <= end_date'),
    )

    employee_no = Column(ForeignKey('employee.employee_no', ondelete='CASCADE'), primary_key=True, nullable=False)
    start_date = Column(Date, primary_key=True, nullable=False)
    end_date = Column(Date)
    job = Column(String(9))
    salary = Column(Integer)
    comm = Column(Integer)
    department_no = Column(ForeignKey('department.department_no', ondelete='SET NULL'))
    chgdesc = Column(String(80))

    department = relationship('Department')
    employee = relationship('Employee')
