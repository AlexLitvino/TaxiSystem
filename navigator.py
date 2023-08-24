"""This module contains Navigator class that responsible for logic performed on city maps"""

import json
import os

maps_path = 'maps'


class Navigator:

    def __init__(self, city):
        self.city = city
        self.map = self.download_map()

    def download_map(self):
        """Downloads map from file"""
        map_file_path = os.path.join(maps_path, f'{self.city}.json')
        with open(map_file_path, 'r') as f:
            return json.load(f)

    def calculate_distance(self, location1, location2):
        """Calculates distance between two locations"""
        return abs(self.get_coordinates(location1) - self.get_coordinates(location2))

    def add_location(self, location, coordinates):
        """Adds new location to map"""
        # TODO: should be added to file as well
        self.map[location] = coordinates

    def get_coordinates(self, location):
        """Returns coordinates for location"""
        try:
            return self.map[location]
        except KeyError:
            raise AddressNotFoundError(f"{location} is not present for {self.city.capitalize()}")

    def get_all_locations(self):
        """Returns all existing locations on map"""
        return list(self.map.keys())

    def is_location_exist(self, location):
        """Returns True if location exists on map"""
        return location in self.map


class AddressNotFoundError(Exception):
    pass
