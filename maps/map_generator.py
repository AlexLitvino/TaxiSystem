import json
import random


# TODO: faker could be used for real-like addresses
def generate_map(city: str, address_count, min_coordinate=0, max_coordinate=35):
    map_ = {f"Address{i}": random.randint(min_coordinate, max_coordinate) for i in range(1, address_count)}
    map_file_name = f"{city}.json"
    with open(map_file_name, 'w') as f:
        json.dump(map_, f, indent=4)


if __name__ == '__main__':
    generate_map('kharkiv', 100)
    generate_map('kyiv', 100)
    generate_map('lviv', 100)
