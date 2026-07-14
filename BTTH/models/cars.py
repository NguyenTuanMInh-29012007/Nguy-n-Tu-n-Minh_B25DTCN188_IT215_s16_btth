from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from enum import Enum


class CarStatus(str, Enum):
    AVAILABLE  = 'AVAILABLE'
    MAINTENANCE = 'MAINTENANCE'


class CarModel(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    license_plate = Column(String(20), nullable=False)
    status = Column(Enum(CarStatus), nullable=False)

    bookings = relationship(
        'BookingModel',
        back_populates='cars'
    )

    driver = relationship(
        'DriverModel',
        secondary='bookings',
        back_populates='cars'
    )
