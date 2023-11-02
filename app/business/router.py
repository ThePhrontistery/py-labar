# File: app/business/router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.business.services.user_service import UserService  # Hypothetical service class
from app.common.infra.database import get_db  # Database session dependency
from app.domain.schemas.poll import PollCreate, PollResponse  # Hypothetical Poll schemas

# Create an APIRouter instance to define the route functions.
router = APIRouter()

@router.get("/polls", response_model=list[PollResponse])
def get_polls(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Retrieve a list of polls from the database.

    Uses dependency injection to obtain a database session.
    Calls the poll service to get the list of polls.
    """
    poll_service = UserService(db)  # Hypothetical service class instance
    polls = poll_service.get_polls(skip=skip, limit=limit)  # Hypothetical service method
    return polls

@router.post("/polls", response_model=PollResponse)
def create_poll(poll: PollCreate, db: Session = Depends(get_db)):
    """
    Create a new poll in the database.

    Accepts a PollCreate schema object that contains the data needed to create a poll.
    Uses dependency injection to obtain a database session.
    Calls the poll service to create the new poll.
    """
    poll_service = UserService(db)  # Hypothetical service class instance
    created_poll = poll_service.create_poll(poll=poll)  # Hypothetical service method
    if created_poll is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Error creating poll")
    return created_poll
