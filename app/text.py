from fastapi import FastAPI, Depends, Form, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app.common.infra.database import SessionLocal, Base, engine
from app.domain.schemas.user import UserCreate, UserResponse
from app.business.services.user_service import get_user_by_username, create_user

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Check if user already exists
    db_user = get_user_by_username(db, username=username)
    if db_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username is already registered"})
    
    # Hash the user password
    hashed_password = pwd_context.hash(password)
    
    # Create new user model instance
    user = UserCreate(username=username, email=email, hashed_password=hashed_password)
    
    # Save the new user to the database
    create_user(db=db, user=user)
    
    # Redirect to login or home page after successful registration
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
