# File: app/common/core/security.py

from passlib.context import CryptContext

# Creating a CryptContext object which uses the "bcrypt" hashing algorithm.
# The "deprecated" parameter is used to automatically handle the migrations to newer hashing algorithms over time.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies a plain password against the hashed password.

    Args:
    - plain_password (str): The plain text password to verify.
    - hashed_password (str): The hashed password to verify against.

    Returns:
    - bool: True if the password is correct, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Hashes a plain password using bcrypt.

    Args:
    - password (str): The plain text password to hash.

    Returns:
    - str: The hashed password.
    """
    return pwd_context.hash(password)
