# File: app/business/controllers/controller.py
"""
The controller.py file in app/business/controllers directory is designed to interact with the service layer, 
which contains the core business logic. In a clean architecture, the controller's role is to take in HTTP requests, 
delegate processing to the services, and then return the appropriate HTTP responses. 
It acts as a glue between the HTTP interface and service layer, 
ensure that the service layer doesn't have to deal with the specifics of HTTP.
"""

from app.Business.services.user_service import create_user_service, get_user_by_id_service, get_all_users_service
from app.domain.schemas.user import UserCreate, UserResponse
from sqlalchemy.orm import Session

def create_user_controller(user: UserCreate, db: Session) -> UserResponse:
    # Use the service layer function to create a new user.
    return create_user_service(db=db, user=user)

def get_user_by_id_controller(user_id: int, db: Session) -> UserResponse:
    # Use the service layer function to retrieve a user by ID.
    return get_user_by_id_service(db=db, user_id=user_id)

def get_all_users_controller(db: Session) -> list[UserResponse]:
    # Use the service layer function to retrieve all users.
    return get_all_users_service(db=db)
