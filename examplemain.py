from fastapi import FastAPI, Form, Depends, HTTPException
from starlette.status import HTTP_303_SEE_OTHER
from starlette.responses import RedirectResponse
from app.business.controllers import UserController  # Import the user controller
from app.common.infra.database import get_db  # Import the database session provider
from sqlalchemy.orm import Session

app = FastAPI()

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user_controller = UserController(db)
    user = user_controller.authenticate_user(username, password)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # If user is authenticated, redirect to home
    response = RedirectResponse(url="/home", status_code=HTTP_303_SEE_OTHER)
    # Here you should set up a secure session or token to keep the user logged in
    # For example, using JWT tokens or secure cookies
    return response