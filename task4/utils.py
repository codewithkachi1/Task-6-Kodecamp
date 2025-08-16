import hashlib
import json
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = "secret_key_here"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)

def generate_token(username):
    payload = {
        "exp": datetime.now(timezone.utc) + timedelta(minutes=30),
        "iat": datetime.now(timezone.utc),
        "sub": username
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
