from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from utils import verify_token

security = HTTPBearer()

def get_current_user(token: HTTPAuthorizationCredentials = Depends(security)):
    username = verify_token(token.credentials)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    return username
