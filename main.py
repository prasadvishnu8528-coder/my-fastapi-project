
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Student data
students = [
    {"id": 1, "name": "Rahul", "branch": "IT"},
    {"id": 2, "name": "Aman", "branch": "CSE"},
    {"id": 3, "name": "Vishnu", "branch": "IT"}
]

# Student model
class Student(BaseModel):
    id: int
    name: str
    branch: str


# Home API
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


# About API
@app.get("/about")
def about():
    return {"name": "My First Backend"}


# Get all students
@app.get("/students")
def get_students():
    return students


# Add new student
@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())

    return {
        "message": "Student added successfully",
        "student": student
    }


@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:
        if student["id"] == student_id:
            return student

    return {"message": "Student not found"}



@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for i in range(len(students)):
        if students[i]["id"] == student_id:

            students[i] = {
                "id": student_id,
                "name": student.name,
                "branch": student.branch
            }

            return {
                "message": "Student updated successfully",
                "student": students[i]
            }

    return {"message": "Student not found"}




@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for i in range(len(students)):
        if students[i]["id"] == student_id:

            deleted_student = students.pop(i)

            return {
                "message": "Student deleted successfully",
                "student": deleted_student
            }

    return {"message": "Student not found"}


