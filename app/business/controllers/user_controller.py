from fastapi import APIRouter

router = APIRouter()

mock_users = [
    {"id": 1, "username": "Usuario1"},
    {"id": 2, "username": "Usuario2"},
    {"id": 3, "username": "Usuario3"},
]

@router.get("/user_data")
def get_users():
    return mock_users

@router.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    user = next((u for u in mock_users if u["id"] == user_id), None)
    if user is None:
        return {"error": "Usuario no encontrado"}
    return user