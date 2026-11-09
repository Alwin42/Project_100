from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from .database import Base

class BookingStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Service(Base):
    __tablename__ = "services"
    
    sid = Column(Integer, primary_key=True, index=True)
    service_title = Column(String(200), nullable=False)
    service_description = Column(Text)
    amount = Column(Float)
    uid = Column(Integer, ForeignKey("users.uid"))
    wid = Column(Integer, ForeignKey("workers.wid"))
    publish_date = Column(DateTime, default=datetime.utcnow)
    expiry_date = Column(DateTime)
    city_town = Column(String(100))
    status = Column(String(50), default="active")
    emergency_type = Column(String(50))
    
    # Relationships
    user = relationship("User", foreign_keys=[uid], back_populates="services_requested")
    worker = relationship("Worker", foreign_keys=[wid], back_populates="services_provided")
    bookings = relationship("Booking", back_populates="service")

class Booking(Base):
    __tablename__ = "bookings"
    
    bid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("users.uid"))
    sid = Column(Integer, ForeignKey("services.sid"))
    wid = Column(Integer, ForeignKey("workers.wid"))
    booking_date = Column(DateTime)
    status = Column(String(50), default="pending")
    amount = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("User", foreign_keys=[uid], back_populates="bookings")
    service = relationship("Service", back_populates="bookings")
    worker = relationship("Worker", foreign_keys=[wid], back_populates="bookings_received")

# Update User model to include relationships
class User(Base):
    __tablename__ = "users"
    
    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    role = Column(String(50), default="user")
    city_town = Column(String(100))
    country = Column(String(100))
    address = Column(Text)
    phone = Column(String(20))
    rating = Column(Float, default=0.0)
    date_of_join = Column(DateTime, default=datetime.utcnow)
    total_spent_on_services = Column(Float, default=0.0)
    total_services_completed = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    
    # Relationships
    services_requested = relationship("Service", foreign_keys="Service.uid", back_populates="user")
    bookings = relationship("Booking", foreign_keys="Booking.uid", back_populates="user")

# Update Worker model
class Worker(Base):
    __tablename__ = "workers"
    
    wid = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    profession = Column(String(100))
    years_of_experience = Column(Integer)
    skills = Column(Text)
    city_town = Column(String(100))
    organisation_individual = Column(String(50))
    total_services_done = Column(Integer, default=0)
    total_money_gained = Column(Float, default=0.0)
    verified_status = Column(Boolean, default=False)
    contact_number = Column(String(20))
    ratings = Column(Float, default=0.0)
    
    # Relationships
    services_provided = relationship("Service", foreign_keys="Service.wid", back_populates="worker")
    bookings_received = relationship("Booking", foreign_keys="Booking.wid", back_populates="worker")