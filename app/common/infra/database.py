# File: app/common/infra/database.py

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
import os

# The DATABASE_URL should be obtained from environment variables for security purposes.
# os.getenv allows us to get the environment variable value.
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# When using SQLite, the following argument can be added to use a StaticPool,
# which is necessary if you're planning to use the app with concurrency.
# For other database engines (e.g., PostgreSQL), you would remove it.
engine_options = {}
if "sqlite" in DATABASE_URL:
    engine_options["connect_args"] = {"check_same_thread": False}
    engine_options["poolclass"] = StaticPool

# Creating the SQLAlchemy engine that will interact with the database.
engine = create_engine(DATABASE_URL, **engine_options)

# Creating a configured "SessionLocal" class which will serve as a factory for
# new Session objects. It's called "SessionLocal" to distinguish it from the
# SQLAlchemy's built-in session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The declarative base class will be used to create database models.
Base = declarative_base()

# Define the User model by inheriting from the Base class.
class User(Base):
    __tablename__ = "users"  # Database table name.

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # Storing hashed passwords

# Methods for handling database operations
def init_db() -> None:
    """
    Initializes the database by creating all tables based on the declarative base.
    """
    Base.metadata.create_all(bind=engine)

def get_db() -> Session:
    """
    Dependency that can be used to get a database session.
    Ensures that the session is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
