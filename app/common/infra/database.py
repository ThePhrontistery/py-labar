# File: app/Common/infra/database.py
# SQLAlchemy is used here as the ORM and Alembic for migrations.
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# The DATABASE_URL should be kept in environment variables for security purposes
# and not hard-coded in your source code.
DATABASE_URL = "sqlite:///./test.db"  # The SQLite database file name.

# Creating the SQLAlchemy engine that will interact with the database.
engine = create_engine(DATABASE_URL)

# Creating a configured "SessionLocal" class which will serve as a factory for
# new Session objects. It's called "SessionLocal" to distinguish it from the
# SQLAlchemy's built-in session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The declarative base class will be used to create database models.
Base = declarative_base()

# Define the User model by inheriting from the Base class.
# This class uses the SQLAlchemy ORM to map the model attributes to the database table.
class User(Base):
    __tablename__ = "users"  # Database table name.

    # Here we define columns for the table user.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, index=True)  # Passwords must be hashed!

# This is a good place to add methods for database initialization, like creating tables.
def init_db():
    # This method will create all tables by using the Base.metadata.create_all method,
    # ensuring that the tables and the database are properly set up.
    Base.metadata.create_all(bind=engine)
