"""This module contains base class User for TaxiSystem users"""


class User:

    def __init__(self, manager, name, date_of_birth):
        self.manager = manager
        self.name = name
        self.date_of_birth = date_of_birth
