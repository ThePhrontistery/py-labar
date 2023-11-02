# File: app/main.py
# Standard library imports
from datetime import datetime, timedelta

# Related third-party imports
from fastapi import Depends, FastAPI, Form, HTTPException, Request, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.orm import Session

# Local application/library-specific imports
from app.business.controllers.controller import UserController
from app.business.services.user_service import authenticate_user, create_user, get_user_by_username_service
from app.common.infra.database import init_db, SessionLocal
from app.domain.schemas.user import UserCreate, UserResponse
from app.common.core.security import get_password_hash

app = FastAPI()

## Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates directory configuration
templates = Jinja2Templates(directory="templates")


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Assuming you have a function to get user data in usercontroller
    # This is just a placeholder
    user_data = "Sample user data"
    user_id = 1
    return templates.TemplateResponse("index.html", {"request": request, "user_data": user_data, "user_id": user_id})


@app.post("/create_user/", response_model=UserResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    return db_user


@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user_controller = UserController(db)
    user = user_controller.authenticate_user(username, password)
    if user is None:
        return templates.TemplateResponse("index.html", {"request": request, "error": "Incorrect username or password"})
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response = RedirectResponse(url="/home", status_code=status.HTTP_303_SEE_OTHER)
    response.set_cookie(
        key="access_token", value=f"Bearer {access_token}", httponly=True
    )
    return response

@app.get("/register", name="register_user")
async def register_user(request: Request):
    # Your registration page logic here
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    db_user = get_user_by_username_service(db, username=username)
    if db_user:
        return templates.TemplateResponse("register.html", {"request": request, "error": "Username is already registered"})
    
    hashed_password = get_password_hash(password)
    user = UserCreate(username=username, email=email, hashed_password=hashed_password)
    create_user(db=db, user=user)
    return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)


@app.get("/forgot-password", name="forgot_password")
async def forgot_password(request: Request):
    # Your forgot password logic here
    return templates.TemplateResponse("forgot_password.html", {"request": request})

@app.post("/forgot-password", name="forgot_password")
async def forgot_password(request: Request, email: str = Form(...)):
    # Your logic to handle password reset (e.g., sending a reset email) goes here
    # ...
    return templates.TemplateResponse("password_reset_sent.html", {"request": request})

# Add additional routes as needed
# ...

# Conditional end block
# to run the application only if this script is executed as the main module.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
