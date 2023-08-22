import json
import os

maps_path = 'maps'


class Navigator:

    def __init__(self, city):
        self.city = city
        self.map = self.download_map()

    def download_map(self):
        map_file_path = os.path.join(maps_path, f'{self.city}.json')
        with open(map_file_path, 'r') as f:
            return json.load(f)

    def calculate_distance(self, location1, location2):
        return abs(self.get_coordinates(location1) - self.get_coordinates(location2))

    def add_location(self, address, coordinates):
        # TODO: should be added to file as well
        self.map[address] = coordinates

    def get_coordinates(self, address):
        try:
            return self.map[address]
        except KeyError:
            raise AddressNotFound(f"{address} is not present for {self.city.capitalize()}")

    def get_all_addresses(self):
        return list(self.map.keys())

    def is_location_exist(self, location):
        return location in self.map


class AddressNotFound(Exception):
    pass
