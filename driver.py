from enum import Enum
from random import choice

import cars
from user import User


class DriverStatus(Enum):
    ACTIVE = 0
    INACTIVE = 1
    ON_RIDE = 2


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

    def take_order(self):
        self.driver_status = DriverStatus.ON_RIDE
        self.manager.remove_driver_from_active(self)

    def complete_order(self):
        self.driver_status = DriverStatus.ACTIVE
        self.manager.move_driver_to_active(self)

    def add_car(self, plate_number: str, car_class, model: str, color):
        self.car = cars.PrivateCar(plate_number, car_class, model, color, self)

    @property
    def current_location(self):
        # temporary solution with getting addresses from manager
        random_address = choice(self.manager._navigator.get_all_addresses())
        return random_address

    def __str__(self):
        return f"Driver {self.name} licence number '{self.licence_number}' on {self.car}"
