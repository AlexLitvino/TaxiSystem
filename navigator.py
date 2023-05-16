class Navigator:

    city = None

    map = {
        'Address1': 4434,
        'Address2': 7347,
        'Address3': 2424,
        'Address4': 5742,
        'Address5': 7434,
        'Address6': 6553,
    }

    def __init__(self, city):
        Navigator.city = city

    @classmethod
    def calculate_distance(cls, location1, location2):
        return abs(cls.map[location1] - cls.map[location2])

    @classmethod
    def add_new_location(cls, address, coordinates):
        cls.map[address] = coordinates

    @classmethod
    def get_coordinates(cls, address):
        try:
            return cls.map[address]
        except KeyError:
            raise AddressNotFound(f"{address} is not present for {cls.city}")

    @classmethod
    def get_all_addresses(cls):
        return list(cls.map.keys())


class AddressNotFound(Exception):
    pass
