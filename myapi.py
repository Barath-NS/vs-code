from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "name": "Barath",
        "age": 20,
        "year": "3rd yr"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudents(BaseModel):
    name: Optional[str]=None
    age: Optional[int]=None
    year: Optional[str]=None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/{student_id}")  # Corrected
def get_student(student_id: int = Path(..., description="The ID of the student")):
    return students[student_id]

@app.get("/get-by-name/")
def get_student(name: Optional[str] = None, test: int = Query(...)):
    if name:
        for sid in students:
            if students[sid]["name"] == name:
                return students[sid]
    return {"Data": "not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudents):
    if student_id not in students:
        return {"Error": "Student does not exist"}

    stored_student = students[student_id]  

    update_data = student.dict(exclude_unset=True)  
    
    stored_student.update(update_data)
    
    return stored_student

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exists"}

    del students[student_id] 
    return{"Message": "Student deleted successfully"}