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
        return abs(self.map[location1] - self.map[location2])

    def add_new_location(self, address, coordinates):
        # TODO: should be added to file as well
        self.map[address] = coordinates

    def get_coordinates(self, address):
        try:
            return self.map[address]
        except KeyError:
            raise AddressNotFound(f"{address} is not present for {self.city}")

    def get_all_addresses(self):
        return list(self.map.keys())


class AddressNotFound(Exception):
    pass
