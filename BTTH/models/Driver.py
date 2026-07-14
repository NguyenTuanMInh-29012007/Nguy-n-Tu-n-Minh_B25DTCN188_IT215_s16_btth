from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from enum import Enum


class DriverStatus(str, Enum):
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'


class DriverModel(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(100), nullable=False)
    status = Column(Enum(DriverStatus), nullable=False)

    fleet_id = Column(Integer, ForeignKey("fleets.id"))

    fleet = relationship(
        'FleetModel',
        back_populates='drivers'
    )

    bookings = relationship(
        'BookingModel',
        back_populates='drivers'
    )

    cars = relationship(
        'CarModel',
        secondary='bookings',
        back_populates='drivers'
    )
