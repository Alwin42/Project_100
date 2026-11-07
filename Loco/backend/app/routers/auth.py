from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, security
from ..database import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.UserResponse)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash the password
    hashed_password = security.get_password_hash(user.password)
    
    # Create new user with matching column names
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed_password,
        role=user.role,
        phone=user.phone,
        city_town=user.city_town,
        country=user.country
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login", response_model=schemas.Token)
def login(credentials: schemas.LoginRequest, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == credentials.email).first()
    
    if not user or not security.verify_password(credentials.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create JWT token including the user's role
    access_token = security.create_access_token(data={"sub": user.email, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}