import hashlib
import json

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_students(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_students(students, filename):
    with open(filename, "w") as f:
        json.dump(students, f)
