from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

# User schemas
class UserBase(BaseModel):
    name: str
    email: EmailStr
    phone: str = ""
    city_town: str = ""
    country: str = ""

class UserCreate(UserBase):
    password: str
    role: str = "user"

class UserResponse(UserBase):
    uid: int
    role: str
    is_active: bool
    date_of_join: datetime
    total_spent_on_services: float = 0.0
    total_services_completed: int = 0

    class Config:
        from_attributes = True

# Booking schemas
class BookingResponse(BaseModel):
    bid: int
    service_title: str
    provider_name: str
    provider_initials: str
    booking_date: Optional[datetime]
    status: str
    amount: float
    created_at: datetime

    class Config:
        from_attributes = True

# Dashboard stats schema
class DashboardStats(BaseModel):
    upcoming_bookings: int
    completed_bookings: int
    total_spent: float
    saved_providers: int

class DashboardData(BaseModel):
    stats: DashboardStats
    upcoming_bookings: List[BookingResponse]
    recent_history: List[BookingResponse]

# Login/Register schemas
class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str