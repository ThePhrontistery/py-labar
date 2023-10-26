from fastapi import FastAPI, HTTPException
from app.domain.models.models import User as UserModel
from app.domain.schemas.user import User, UserCreate
from app.database import  SessionLocal
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(content={"error": "Ha ocurrido un error"}, status_code=exc.status_code)


mock_users = [
    {"id": 1, "username": "pchocron", "name": "Paola Chocron"},
    {"id": 2, "username": "jjarbona", "name": "Juan Arbona"},
    {"id": 3, "username": "andsanchez", "name": "Andrés Sánchez"},
]

@app.get("/user_data")
def get_users_mock():
    """
    This route (endpoint) allows a client to retrieve all user data from the mock dataset. The path for this endpoint is //user_data
    Retrieve the list of all users from the mock dataset.
    Returns: A list of dictionaries, where each dictionary represents a user's information.
    """
    return mock_users

@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    """
    Retrieve a specific user's information by their ID.
    Args: user_id (int): The ID of the user to retrieve.
    Returns:  A dictionary containing the user's information or an error message if not found.
    """
    user = next((u for u in mock_users if u["id"] == user_id), None)
    if user is None:
        return "Usuario no encontrado"
    return user


@app.post("/user/", response_model=User)
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = UserModel(username=user.username, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return {"message": "Usuario creado exitosamente"}

@app.get("/users/", response_model=list[User])
def get_users():
    db = SessionLocal()
    users = db.query(UserModel).all()
    db.close()
    return users