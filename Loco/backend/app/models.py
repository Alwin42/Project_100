from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    uid = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    city_town = Column(String(100))
    country = Column(String(100))
    address = Column(Text)
    phone = Column(String(20))
    rating = Column(Float, default=0.0)
    date_of_join = Column(DateTime, default=datetime.utcnow)
    total_spent_on_services = Column(Float, default=0.0)
    total_services_completed = Column(Integer, default=0)
    
    # Relationships
    services_requested = relationship("Service", foreign_keys="Service.uid", back_populates="user")
    payments = relationship("Payment", foreign_keys="Payment.uid", back_populates="user")
    history = relationship("History", foreign_keys="History.uid", back_populates="user")


class Worker(Base):
    __tablename__ = "workers"
    
    wid = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    profession = Column(String(100))
    years_of_experience = Column(Integer)
    skills = Column(Text)  # Store as comma-separated or JSON
    city_town = Column(String(100))
    organisation_individual = Column(String(50))  # 'Organisation' or 'Individual'
    total_services_done = Column(Integer, default=0)
    total_money_gained = Column(Float, default=0.0)
    verified_status = Column(Boolean, default=False)
    contact_number = Column(String(20))
    ratings = Column(Float, default=0.0)
    
    # Relationships
    services_provided = relationship("Service", foreign_keys="Service.wid", back_populates="worker")
    payments_received = relationship("Payment", foreign_keys="Payment.wid", back_populates="worker")


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
    status = Column(String(50))  # e.g., 'Active', 'Completed', 'Cancelled'
    emergency_type = Column(String(50))  # 'Emergency', 'Urgent', 'Normal'
    
    # Relationships
    user = relationship("User", foreign_keys=[uid], back_populates="services_requested")
    worker = relationship("Worker", foreign_keys=[wid], back_populates="services_provided")
    payments = relationship("Payment", back_populates="service")


class Payment(Base):
    __tablename__ = "payments"
    
    pid = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    worker_name = Column(String(100))
    status = Column(String(50))  # 'Pending', 'Completed', 'Failed'
    sid = Column(Integer, ForeignKey("services.sid"))
    date = Column(DateTime, default=datetime.utcnow)
    time = Column(String(20))  # Store time as string or use DateTime
    amount = Column(Float)
    uid = Column(Integer, ForeignKey("users.uid"))
    wid = Column(Integer, ForeignKey("workers.wid"))
    payment_method = Column(String(50))  # 'Cash', 'Card', 'UPI', etc.
    
    # Relationships
    user = relationship("User", foreign_keys=[uid], back_populates="payments")
    worker = relationship("Worker", foreign_keys=[wid], back_populates="payments_received")
    service = relationship("Service", back_populates="payments")


class History(Base):
    __tablename__ = "history"
    
    hid = Column(Integer, primary_key=True, index=True)
    uid = Column(Integer, ForeignKey("users.uid"))
    service_title = Column(String(200))
    service_description = Column(Text)
    username = Column(String(100))
    worker_name = Column(String(100))
    date = Column(DateTime, default=datetime.utcnow)
    payment_amount = Column(Float)
    payment_status = Column(String(50))  # 'Paid', 'Unpaid', 'Refunded'
    
    # Relationships
    user = relationship("User", foreign_keys=[uid], back_populates="history")