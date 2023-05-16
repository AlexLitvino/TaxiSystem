from cars import CarClass, Color
from client import Client
from manager import Manager
from driver import Driver
from navigator import Navigator

navigator = Navigator("Kharkiv")
manager = Manager(navigator)  # creating manager to rule them all

# creating drivers
driver1 = Driver(manager, name='John', date_of_birth=1974, licence_number='QQ324232')
driver1.add_car(plate_number='QW464', car_class=CarClass.Economy, model='Lanos', color=Color.BLUE)
driver1.look_for_order()

driver2 = Driver(manager, name='James', date_of_birth=1997, licence_number='TG6446533')
driver2.add_car(plate_number='AB5476', car_class=CarClass.Economy, model='Reno', color=Color.GRAY)
driver2.look_for_order()

driver3 = Driver(manager, name='Thomas', date_of_birth=1934, licence_number='SF564474')
driver3.add_car(plate_number='AB5476', car_class=CarClass.Economy, model='Volkswagen', color=Color.GRAY)
driver3.look_for_order()

# creating client
client1 = Client(manager, 'Olga', 1995)

# Flow
client1.make_order("Address1", CarClass.Economy)
