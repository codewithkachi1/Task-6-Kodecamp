from fastapi import FastAPI, HTTPException, Depends
from auth import get_current_user
from models import User, Note
from utils import load_data, save_data, hash_password, generate_token

app = FastAPI()

users_filename = "users.json"
notes_filename = "notes.json"

@app.post("/login/")
def login(username: str, password: str):
    users = load_data(users_filename)
    user = users.get(username)
    if not user or user["password"] != hash_password(password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = generate_token(username)
    return {"token": token}

@app.post("/notes/")
def add_note(title: str, content: str, date: str, username: str = Depends(get_current_user)):
    notes = load_data[notes_filename]
    if username not in notes:
        notes[username] = []
    notes[username].append(Note(title, content, date).to_dict())
    save_data(notes, notes_filename)
    return {"message": "Note added successfully"}

@app.get("/notes/")
def get_notes(username: str = Depends(get_current_user)):
    notes = load_data(notes_filename)
    return notes.get(username, [])

