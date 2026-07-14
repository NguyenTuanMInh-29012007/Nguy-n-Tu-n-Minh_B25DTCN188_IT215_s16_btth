from database import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class BookingModel(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))

    drivers = relationship(
        'DriverModel',
        back_populates='bookings'
    )

    car = relationship(
        'CarModel',
        back_populates='bookings'
    )