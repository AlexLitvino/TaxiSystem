from enum import Enum
from random import choice
import time

import cars
from user import User
from utilities import hours_to_minutes


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
        self.current_location = self._generate_random_initial_location()

    def look_for_order(self):
        self.driver_status = DriverStatus.ACTIVE
        self.manager.move_driver_to_active(self)

    def stop_working(self):
        self.driver_status = DriverStatus.INACTIVE
        self.manager.remove_driver_from_active()

    def take_order(self):
        self.driver_status = DriverStatus.ON_RIDE
        self.manager.remove_driver_from_active(self)

    def calculate_time_to_client(self, client_departure):
        time_to_client = self.manager._navigator.calculate_distance(client_departure, self.current_location) / self.car.speed
        return hours_to_minutes(time_to_client)

    def calculate_time_from_client_to_destination(self, departure, destination):
        time_from_client_to_destination = self.manager._navigator.calculate_distance(departure, destination) / self.car.speed
        return hours_to_minutes(time_from_client_to_destination)

    def ride_simulation(self, client_departure, destination):
        time_to_client = self.calculate_time_to_client(client_departure)
        time_from_client_to_destination = self.calculate_time_from_client_to_destination(client_departure, destination)
        print(time_to_client)
        print(time_from_client_to_destination)
        time.sleep(time_to_client)
        time.sleep(time_from_client_to_destination)

    def complete_order(self, destination):
        self.driver_status = DriverStatus.ACTIVE
        self.manager.move_driver_to_active(self)
        self.current_location = destination

    # TODO: should be run in separate thread
    def perform_order(self, departure, destination):
        self.take_order()
        self.ride_simulation(departure, destination)
        self.complete_order(destination)

    def add_car(self, plate_number: str, car_class, model: str, color):
        self.car = cars.PrivateCar(plate_number, car_class, model, color, self)

    def _generate_random_initial_location(self):
        # temporary solution with getting addresses from manager
        random_address = choice(self.manager._navigator.get_all_addresses())
        return random_address

    def __str__(self):
        return f"Driver {self.name} licence number '{self.licence_number}' on {self.car}"
