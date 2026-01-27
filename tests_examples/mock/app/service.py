# service.py
from app.client import fetch_user

def get_username(user_id: int) -> str:
    user = fetch_user(user_id)
    return user["name"]
