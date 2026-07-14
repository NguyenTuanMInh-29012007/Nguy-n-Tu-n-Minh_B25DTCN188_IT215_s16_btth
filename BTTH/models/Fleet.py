from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class FleetModel(Base):
    __tablename__ = 'fleets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    drivers = relationship(
        'DriverModel',
        back_populates='fleets'
    )