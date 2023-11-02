# File: app/business/controllers/controller.py
"""
The controller.py file in app/business/controllers directory is designed to interact with the service layer, 
which contains the core business logic. In a clean architecture, the controller's role is to take in HTTP requests, 
delegate processing to the services, and then return the appropriate HTTP responses. 
It acts as a glue between the HTTP interface and service layer, 
ensure that the service layer doesn't have to deal with the specifics of HTTP.
"""
import bcrypt
from sqlalchemy.orm import Session
from app.domain.models.models import User

from app.business.services.user_service import create_user, get_user_by_id_service, get_all_users_service
from app.domain.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session

def create_user_controller(user: UserCreate, db: Session) -> UserResponse:
    # Use the service layer function to create a new user.
    return create_user(db=db, user=user)

def get_user_by_id_controller(user_id: int, db: Session) -> UserResponse:
    # Use the service layer function to retrieve a user by ID.
    return get_user_by_id_service(db=db, user_id=user_id)

def get_all_users_controller(db: Session) -> list[UserResponse]:
    # Use the service layer function to retrieve all users.
    return get_all_users_service(db=db)

class UserController:
    def __init__(self, db: Session):
        self.db = db

    def authenticate_user(self, username: str, password: str):
        # Query the user by username
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            return None
        
        # Verify the password (ensure the stored password in the database is hashed)
        if bcrypt.checkpw(password.encode('utf-8'), user.hashed_password.encode('utf-8')):
            return user
        else:
            return None