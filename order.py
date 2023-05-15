# Not used
# class Address:
#
#     def __init__(self, city, street, building):
#         self.city = city
#         self.street = street
#         self.building = building
#
#
# class Ride:
#
#     def __init__(self, client, driver, car, departure: Address, arrival: Address):
#         self.client = client
#         self.driver = driver
#         self.car = car # how car and driver is connected?
#         self.departure = departure
#         self.arrival = arrival
#
#     def calculate_price(self):
#         """calculate price depending on deprature, arrival and car class"""
#         pass
#
#
# class Order:
#
#     def __init__(self):
#         self.rides = []
#
#     def calculate_total_price(self):
#         total = 0
#         for ride in self.rides:
#             total += ride.price
#         return total