from fastapi import APIRouter, Depends, HTTPException
from app.utils.jwt_utils import create_jwt_token

auth_router = APIRouter()

users_db = {
    "admin": "password123"
}

@auth_router.post("/login")
def login(username: str, password: str):
    if users_db.get(username) == password:
        token = create_jwt_token({"username": username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid username or password")
