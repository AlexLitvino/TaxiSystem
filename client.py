import random

import user
from navigator import AddressNotFound


class Client(user.User):

    def __init__(self, manager, name, date_of_birth):
        super().__init__(manager, name, date_of_birth)
        self.total_spent_money = 0
        self.total_distance = 0  # TODO: add distance calculation for bonuses
        self.current_location = None

    def calculate_discount(self):
        pass

    def set_current_location(self):
        pass

    def make_order(self, destination, car_class):
        try:
            found_driver = self.manager.looking_for_car(destination, car_class)
            if found_driver:
                print(f"{found_driver.name} will be in {random.randint(4, 9)} minutes\n"
                      f"{found_driver.car.color.name} {found_driver.car.model} {found_driver.car.plate_number}")
            else:
                print("No driver was found:(")
        except AddressNotFound as e:
            print(e)
