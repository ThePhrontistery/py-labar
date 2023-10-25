from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configura la URL de conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:postgre_2023@localhost:5432/ai_labar"

# Crea una instancia del motor SQLAlchemy
engine = create_engine(DATABASE_URL)

# Crea una sesión de SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crea una instancia de Base para declarar modelos SQLAlchemy
Base = declarative_base()