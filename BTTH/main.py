from fastapi import FastAPI

from database import Base, engine

from models.Fleet import FleetModel
from models.Driver import DriverModel
from models.cars import CarModel
from models.booking import BookingModel

app = FastAPI()
Base.metadata.create_all(bind=engine)


# Fleet - Driver : 1 - N
# Driver - Car : N - N


# 1. ForeignKey fleet_id đặt trong bảng Driver vì một Fleet quản lý nhiều Driver
# 2. Quan hệ nhiều - nhiều giữa Driver và Car được thực hiện thông qua bảng Booking
