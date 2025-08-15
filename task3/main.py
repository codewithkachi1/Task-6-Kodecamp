from fastapi import FastAPI, HTTPException, Depends
from auth import security, authenticate_user
from models import JobApplication
from utils import load_data, save_data

app = FastAPI()

applications_filename = "applications.json"

@app.post("/applications/")
def add_application(job_title: str, company: str, date_applied: str, status: str, username: str = Depends(authenticate_user)):
    applications = load_data(applications_filename)
    if username not in applications:
        applications[username] = []
    applications[username].append(JobApplication(job_title, company, date_applied, status).to_dict())
    save_data(applications, applications_filename)
    return {"message": "Job application added successfully"}

@app.get("/applications/")
def get_applications(username: str = Depends(authenticate_user)):
    applications = load_data(applications_filename)
    return applications.get(username, [])