import fastapi
from fastapi import Depends
from sqlalchemy.orm.session import Session

from . import db
from . import schema

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}


@app.get("/department")
async def get_department(session: Session = Depends(db.get_session)):
    return [
        {
            "departmentNo": elm.department_no,
            "department_name": elm.department_name,
        }
        for elm in session.query(schema.Department).all()
    ]
