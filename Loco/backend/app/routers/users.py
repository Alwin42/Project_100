from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import get_db
from ..dependencies import get_current_user # Import the dependency we just made

router = APIRouter()

@router.get("/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    # FastAPI automatically converts the SQLAlchemy model to the Pydantic schema
    # The schema excludes the hashed_password, keeping it secure
    return current_user