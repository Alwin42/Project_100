from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db
from ..dependencies import get_current_user

router = APIRouter()

@router.get("/", response_model=schemas.DashboardData)
def get_dashboard_data(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    # 1. Calculate Stats safely in Python
    upcoming_count = db.query(models.Booking).filter(
        models.Booking.uid == current_user.uid,
        models.Booking.status.in_(["pending", "confirmed"])
    ).count()
    
    completed_bookings = db.query(models.Booking).filter(
        models.Booking.uid == current_user.uid,
        models.Booking.status == "completed"
    ).all()
    
    completed_count = len(completed_bookings)
    total_spent = sum(float(b.amount or 0.0) for b in completed_bookings)
    
    stats_data = schemas.DashboardStats(
        upcoming_bookings=upcoming_count,
        completed_bookings=completed_count,
        total_spent=total_spent,
        saved_providers=0
    )
    
    # 2. Get Upcoming Bookings
    upcoming_db = db.query(models.Booking).join(
        models.Service
    ).join(
        models.Worker
    ).filter(
        models.Booking.uid == current_user.uid,
        models.Booking.status.in_(["pending", "confirmed"])
    ).order_by(models.Booking.booking_date.asc()).limit(5).all()
    
    upcoming_list = []
    for b in upcoming_db:
        initials = "".join([name[0] for name in b.worker.name.split() if name]).upper()
        upcoming_list.append(schemas.BookingResponse(
            bid=b.bid,
            service_title=b.service.service_title,
            provider_name=b.worker.name,
            provider_initials=initials,
            booking_date=b.booking_date,
            status=b.status,
            amount=float(b.amount or 0.0),
            created_at=b.created_at
        ))
        
    # 3. Get Recent History
    history_db = db.query(models.Booking).join(
        models.Service
    ).join(
        models.Worker
    ).filter(
        models.Booking.uid == current_user.uid,
        models.Booking.status == "completed"
    ).order_by(models.Booking.created_at.desc()).limit(5).all()
    
    history_list = []
    for b in history_db:
        initials = "".join([name[0] for name in b.worker.name.split() if name]).upper()
        history_list.append(schemas.BookingResponse(
            bid=b.bid,
            service_title=b.service.service_title,
            provider_name=b.worker.name,
            provider_initials=initials,
            booking_date=b.booking_date,
            status=b.status,
            amount=float(b.amount or 0.0),
            created_at=b.created_at
        ))
        
    return schemas.DashboardData(
        stats=stats_data,
        upcoming_bookings=upcoming_list,
        recent_history=history_list
    )