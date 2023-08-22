"""This module contains class Client that encapsulates logic for Taxi System client"""

import user
from navigator import AddressNotFound


class Client(user.User):

    def __init__(self, manager, name, date_of_birth):
        super().__init__(manager, name, date_of_birth)
        self.current_location = None

    def set_current_location(self, address):
        self.manager.validate_location(address)
        self.current_location = address

    def make_order(self, destination, car_class):
        try:
            self.manager.validate_location(destination)

            found_driver = self.manager.looking_for_car(self.current_location, car_class)
            if found_driver:
                time_to_client = found_driver.calculate_time_to_client(self.current_location)
                print(f"{found_driver.name} will be in {time_to_client} minutes\n"
                      f"{found_driver.car.color.name} {found_driver.car.model} {found_driver.car.plate_number}")
            else:
                print("No driver was found:(")
            found_driver.perform_order(self.current_location, destination)
        except AddressNotFound as e:
            print(e)
