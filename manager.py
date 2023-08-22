import random
from typing import List

import cars
from driver import Driver
from navigator import AddressNotFound
from utilities import hours_to_minutes


class Manager:
    instance = None

    # making Manager instance is singleton
    def __new__(cls, *args, **kwargs):
        if Manager.instance:
            return Manager.instance
        else:
            instance = super().__new__(Manager)
            return instance

    def __init__(self, navigator):
        if Manager.instance:
            pass
        else:
            self.clients = []
            self.drivers = []
            self.active_drivers: List[Driver] = []
            self._navigator = navigator
            Manager.instance = self

    def move_driver_to_active(self, driver: Driver):
        self.active_drivers.append(driver)

    def remove_driver_from_active(self, driver: Driver):
        self.active_drivers.remove(driver)

    def looking_for_car(self, departure, desired_car_class: cars.CarClass):
        """Returns the closest driver to destination with specified car class"""
        active_drivers_of_desired_car_class = [driver for driver in self.active_drivers if driver.car.car_class == desired_car_class]
        found_drivers = [active_drivers_of_desired_car_class[0]]
        min_distance = self._navigator.calculate_distance(found_drivers[0].current_location, departure)
        for driver in active_drivers_of_desired_car_class:
            distance = self._navigator.calculate_distance(driver.current_location, departure)
            if distance < min_distance:
                min_distance = distance
                found_drivers.clear()
                found_drivers.append(driver)
            elif distance == min_distance:
                found_drivers.append(driver)

        if not found_drivers:
            raise DriverNotFound

        driver = random.choice(found_drivers)  # if found several drivers on the same distance, choose random

        return driver

    def get_active_drivers(self):
        return self.active_drivers

    def validate_location(self, location):
        if not self._navigator.is_location_exist(location):
            raise AddressNotFound(f"{location} is not present for {self._navigator.city.capitalize()}")

    def calculate_time_for_distance(self, departure, destination, speed):
        time_in_hours = self._navigator.calculate_distance(departure, destination) / speed
        return hours_to_minutes(time_in_hours)


class DriverNotFound(Exception):
    pass
