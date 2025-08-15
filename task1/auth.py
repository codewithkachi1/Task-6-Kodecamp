from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils import hash_password, load_students

security = HTTPBasic()

def get_student(username, filename):
    students = load_students(filename)
    return students.get(username)

def authenticate_student(credentials: HTTPBasicCredentials = Depends(security), filename="students.json"):
    student = get_student(credentials.username, filename)
    if not student or student["password"] != hash_password(credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username
