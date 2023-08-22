from enum import Enum
import random

from driver import Driver


class CarClass(Enum):
    Luxury = 1
    Business = 2
    Economy = 3


class Color(Enum):
    BLACK = 1
    RED = 2
    GREEN = 3
    BLUE = 4
    GRAY = 5


class Car:

    def __init__(self, plate_number: str, car_class: CarClass, model: str, color: Color):
        self.plate_number = plate_number
        self.car_class = car_class
        self.model = model
        self.color = color
        self.speed = 40 + (60 - 40) * random.random()  # set random speed in range [40 ... 60]

    def __str__(self):
        return f"{self.color.name.lower()} {self.model} '{self.plate_number}' {self.car_class.name.lower()} class"


class PrivateCar(Car):

    def __init__(self, plate_number: str, car_class: CarClass, model: str, color: Color, owner: Driver):
        super().__init__(plate_number, car_class, model, color)
        self.owner = owner
