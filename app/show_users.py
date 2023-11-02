# File: app/show_users.py
# This is run as a standalone script.

from sqlalchemy.orm import Session
from app.common.infra.database import SessionLocal, User, init_db

# Initialize the database (create tables if they don't exist).
init_db()

# Create a new session to interact with the database.
with SessionLocal() as session:
    # Query the User table to retrieve all records.
    users = session.query(User).all()
    
    # Print out the details of each user.
    for user in users:
        print(f"User ID: {user.id}, Username: {user.username}, Email: {user.email}")
