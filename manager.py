"""This module contains Manager class that responsible for communication between Clients and Drivers"""

import random
from typing import List

import cars
from driver import Driver
from navigator import AddressNotFoundError
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
            self.rides_threads = []
            self._navigator = navigator
            Manager.instance = self

    def add_driver_to_active(self, driver: Driver):
        """Adds driver to list of active drivers (those who are ready to take an order)"""
        self.active_drivers.append(driver)

    def remove_driver_from_active(self, driver: Driver):
        """Removed driver from active drivers (when driver serves the order or finishes working)"""
        self.active_drivers.remove(driver)

    def looking_for_car(self, departure, desired_car_class: cars.CarClass):
        """Returns the closest driver to destination with specified car class"""
        active_drivers_of_desired_car_class = [driver for driver in self.active_drivers if driver.car.car_class == desired_car_class]
        # finding the nearest drivers to the client
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
        """Returns list of drivers ready to take orders"""
        return self.active_drivers

    def validate_location(self, location):
        """Raises AddressNotFoundError exception if location can't be find in city map"""
        if not self._navigator.is_location_exist(location):
            raise AddressNotFoundError(f"{location} is not present for {self._navigator.city.capitalize()}")

    def calculate_time_for_distance(self, departure, destination, speed):
        """Calculates time in minutes need to drive from departure to destination with speed"""
        time_in_hours = self._navigator.calculate_distance(departure, destination) / speed
        return hours_to_minutes(time_in_hours)

    def wait_for_all_rides_to_complete(self):
        """Waits till all rides will complete"""
        for thread in self.rides_threads:
            thread.join()


class DriverNotFound(Exception):
    pass
