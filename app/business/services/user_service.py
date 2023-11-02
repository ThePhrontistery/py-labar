# File: app/business/services/user_service.py

from app.common.infra.database import SessionLocal, User
from app.domain.schemas.user import UserCreate
from sqlalchemy.orm import Session
from typing import List, Optional

from app.common.core.security import get_password_hash, verify_password
from app.common.infra.database import User

# This function creates a new user with a hashed password.
def create_user(db: Session, user: UserCreate) -> User:
    """
    Create a new user in the database with a hashed password.
    """
    hashed_password = get_password_hash(user.password)
    db_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_username_service(db: Session, username: str) -> User:
    """
    Retrieve a user by their username.

    Parameters:
    - db: Session - The database session used to perform the query.
    - username: str - The username of the user to retrieve.

    Returns:
    - User: The User object if found, otherwise None.
    """
    return db.query(User).filter(User.username == username).first()    

# This function authenticates a user by verifying the password.
def authenticate_user(db: Session, username: str, password: str) -> User | None:
    """
    Authenticate a user by their username and password.

    This function attempts to authenticate a user by querying the User model
    with the provided username. If a user with the given username exists and
    the provided password matches the hashed password in the database, the User
    object is returned; otherwise, None is returned.

    Parameters:
    - db: Session - The database session used to perform the query.
    - username: str - The username of the user to authenticate.
    - password: str - The plaintext password provided for authentication.

    Returns:
    - Optional[User]: The authenticated User object, or None if authentication fails.
    """
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

# This function retrieves a user by their ID.
def get_user_by_id_service(db: Session, user_id: int) -> Optional[User]:
    """
    Retrieve a user by their unique ID.

    Parameters:
    - db: Session - The database session used to perform the query.
    - user_id: int - The unique identifier of the user to retrieve.

    Returns:
    - Optional[User]: The User object if found, otherwise None.
    """
    return db.query(User).filter(User.id == user_id).first()

# This function retrieves all users.
def get_all_users_service(db: Session) -> List[User]:
    """
    Retrieve all users from the database.

    Parameters:
    - db: Session - The database session used to perform the query.

    Returns:
    - List[User]: A list of User objects.
    """
    return db.query(User).all()
