"""This module contains class Client that encapsulates logic for Taxi System client"""

import user
from navigator import AddressNotFoundError


class Client(user.User):

    def __init__(self, manager, name, date_of_birth):
        super().__init__(manager, name, date_of_birth)
        self.current_location = None

    def set_current_location(self, location):
        """Set current location for Client"""
        self.manager.validate_location(location)
        self.current_location = location

    def make_order(self, destination, car_class):
        """Makes order to get to destination on car of car_class level"""
        print(f"{self.name} ordering taxi of {car_class.name} class from {self.current_location} to {destination}")
        try:
            self.manager.validate_location(destination)

            found_driver = self.manager.looking_for_car(self.current_location, car_class)
            if found_driver:
                time_to_client = found_driver.calculate_time_to_client(self.current_location)
                print(f"{found_driver.name} will be in {time_to_client} minutes\n"
                      f"{found_driver.car.color.name} {found_driver.car.model} {found_driver.car.plate_number}")
            else:
                print("No driver was found:(")
            #found_driver.perform_order(self.current_location, destination)
            #print(f"Order for {self.name} is completed")

            from threading import Thread
            thread = Thread(target=found_driver.perform_order, args=(self.current_location, destination, self.name))
            self.manager.rides_threads.append(thread)
            thread.start()

        except AddressNotFoundError as e:
            print(e)
