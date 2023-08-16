from typing import List

import cars
from driver import Driver


class Manager:
    instance = None

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

    def looking_for_car(self, destination: str, desired_car_class: cars.CarClass):
        """Returns the closest driver to destination with specified car class"""
        # TODO: when driver is found, should it be set to inactive?
        # TODO: what if several drivers are ok?
        driver = min([driver for driver in self.active_drivers if driver.car.car_class == desired_car_class],
                     key=lambda driver: self._navigator.calculate_distance(driver.current_location, destination),
                     default=None)
        if not driver:
            raise DriverNotFound
        return driver


class DriverNotFound(Exception):
    pass
