from fastapi import Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils import hash_password, load_data

security = HTTPBasic()

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security), filename="users.json"):
    users = load_data(filename)
    user = users.get(credentials.username)
    if not user or user["password"] != hash_password(credentials.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username
