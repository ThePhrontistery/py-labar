from fastapi import Depends, FastAPI, Form, HTTPException, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.common.infra.database import SessionLocal, Base, engine
from app.domain.schemas.user import UserCreate, UserResponse
from app.business.services.user_service import create_user, authenticate_user
from app.business.controllers.controller import UserController
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

# Secret key to encode JWT - should be kept secret and safe
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Jinja2 templates directory configuration
templates = Jinja2Templates(directory="templates")

# Initialize database tables
Base.metadata.create_all(bind=engine)

#Upon successful authentication, generate a JWT token to maintain the user session.
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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

@app.post("/register", name="register_user")
async def register_user(request: Request, username: str = Form(...), email: str = Form(...), password: str = Form(...)):
    # Your logic to handle user registration goes here
    # ...
    return templates.TemplateResponse("registration_successful.html", {"request": request})

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

# If you're going to use this file as a script, you might want to add a conditional block
# to run the application only if this script is executed as the main module.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
