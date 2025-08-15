from fastapi import FastAPI, HTTPException, Depends
from auth import security, authenticate_student
from models import Student
from utils import load_students, save_students, hash_password

app = FastAPI()

filename = "students.json"

@app.post("/register/")
def register_student(username: str, password: str):
    students = load_students(filename)
    if username in students:
        raise HTTPException(status_code=400, detail="Student already exists")
    students[username] = Student(username, hash_password(password), []).to_dict()
    save_students(students, filename)
    return {"message": "Student registered successfully"}

@app.post("/login/")
def login_student(username: str = Depends(authenticate_student)):
    return {"message": "Student logged in successfully"}

@app.get("/grades/")
def get_grades(username: str = Depends(authenticate_student)):
    students = load_students(filename)
    return students[username]["grades"]
