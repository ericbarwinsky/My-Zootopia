import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
      return json.load(handle)


def print_data_fox_in_json(animals_data):
    for data in animals_data:
        try:
            print(f"Name: {data["name"]}")
            print(f"Diet: {data["characteristics"]["diet"]}")
            print(f"Location: {data["locations"][0]}")
            print(f"Type: {data["characteristics"]["type"]}")
            print("")
        except KeyError:
            print("")
            pass





animals_data = load_data('animals_data.json')
print_data_fox_in_json(animals_data)