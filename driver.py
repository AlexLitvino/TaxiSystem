from enum import Enum
from random import choice

import cars
from user import User


class DriverStatus(Enum):
    ACTIVE = 0
    INACTIVE = 1


class Driver(User):

    def __init__(self, manager, name, date_of_birth, licence_number):
        super().__init__(manager, name, date_of_birth)
        self.licence_number = licence_number
        self.car = None
        self.driver_status = DriverStatus.INACTIVE

    def look_for_order(self):
        self.driver_status = DriverStatus.ACTIVE
        self.manager.move_driver_to_active(self)

    def stop_working(self):
        self.driver_status = DriverStatus.INACTIVE
        self.manager.remove_driver_from_active()

    def add_car(self, plate_number: str, car_class, model: str, color):
        self.car = cars.PrivateCar(plate_number, car_class, model, color, self)

    @property
    def current_location(self):
        random_address = choice(self.manager.navigator.get_all_addresses())
        return random_address
