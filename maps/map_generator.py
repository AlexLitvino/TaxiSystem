import json
import random


# TODO: faker could be used for real-like addresses
def generate_map(city: str, address_count):
    map_ = {f"Address{i}": random.randint(1000, 9999) for i in range(1, address_count)}
    map_file_name = f"{city}.json"
    with open(map_file_name, 'w') as f:
        json.dump(map_, f, indent=4)


if __name__ == '__main__':
    generate_map('kharkiv', 100)
    generate_map('kyiv', 100)
    generate_map('lviv', 100)
