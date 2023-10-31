# File: app/business/services/user_service.py

from passlib.context import CryptContext
from app.common.infra.database import SessionLocal, User
from app.domain.schemas.user import UserCreate
from sqlalchemy.orm import Session
from typing import List, Optional

# This context is used for hashing and verifying passwords.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# This function creates a new user with a hashed password.
def create_user_service(db: Session, user: UserCreate) -> User:
    """
    Create a new user in the database.

    This service function takes a SQLAlchemy Session and a UserCreate schema object,
    creates a new User model instance with a hashed password, and adds it to the database.
    It commits the session to save the user and refreshes the instance from the database.

    Parameters:
    - db: Session - The database session used to perform the transaction.
    - user: UserCreate - The schema object containing the user's username, email, and plaintext password.

    Returns:
    - User: The newly created User model instance, now with a database-generated ID and hashed password.
    
    Note:
    - This function assumes the existence of a `get_password_hash` function to hash the password.
    """
    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=get_password_hash(user.password),  # Assuming the field is `hashed_password` and not `password`.
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# This function authenticates a user by verifying the password.
def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
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
    if not user or not verify_password(password, user.hashed_password):  # Assuming the field is `hashed_password`.
        return None
    return user

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
