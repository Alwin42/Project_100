from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine, Base
from .routers import auth

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Loco API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/api/auth", tags=["Authentication"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Loco API"}