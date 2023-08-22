"""Example of TaxiSystem usage"""

from cars import CarClass, Color
from client import Client
from manager import Manager
from driver import Driver
from navigator import Navigator

navigator = Navigator("kharkiv")
manager = Manager(navigator)  # creating manager to rule them all

# creating drivers (create driver, add car for him and set him to searching for orders)
driver1 = Driver(manager, name='John', date_of_birth=1974, licence_number='QQ324232')
driver1.add_car(plate_number='QW464', car_class=CarClass.Economy, model='Lanos', color=Color.BLUE)
driver1.look_for_order()

driver2 = Driver(manager, name='James', date_of_birth=1997, licence_number='TG6446533')
driver2.add_car(plate_number='AB5476', car_class=CarClass.Economy, model='Reno', color=Color.GRAY)
driver2.look_for_order()

driver3 = Driver(manager, name='Thomas', date_of_birth=1934, licence_number='SF564474')
driver3.add_car(plate_number='DF4526', car_class=CarClass.Economy, model='Volkswagen', color=Color.GRAY)
driver3.look_for_order()

driver4 = Driver(manager, name='Andrew', date_of_birth=1956, licence_number='JH450245')
driver4.add_car(plate_number='KJ5367', car_class=CarClass.Economy, model='Audi', color=Color.GREEN)
driver4.current_location = 'Address6'
driver4.look_for_order()

driver5 = Driver(manager, name='Thomas', date_of_birth=1963, licence_number='HA349382')
driver5.add_car(plate_number='KA3901', car_class=CarClass.Economy, model='Honda', color=Color.RED)
driver5.current_location = 'Address6'
driver5.look_for_order()


# creating client
client1 = Client(manager, 'Olga', 1995)
client2 = Client(manager, 'Igor', 2000)
client3 = Client(manager, 'Andrew', 2000)


# Application flow

# Show active drivers before any orders
for driver in manager.get_active_drivers():
    print(driver)
print()

# Make order for existing address
client1.set_current_location("Address2")
client1.make_order("Address1", CarClass.Economy)
print()

# Make order for unknown destination address
client2.set_current_location("Address5")
client2.make_order("Unknown address", CarClass.Economy)
print()

# Make order for unknown destination address
client3.set_current_location("Address6")
client3.make_order("Address8", CarClass.Economy)
print()


# Show active drivers after making orders
for driver in manager.get_active_drivers():
    print(driver)
print()
