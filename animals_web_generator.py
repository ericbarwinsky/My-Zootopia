import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
      return json.load(handle)


def print_data_fox_in_json(animals_data):
    """
        Parses a list of animal data dictionaries and formats it into a readable string.
        Input: json (list[dict])
        Returns:
        str: A formatted string containing the name, diet, first location, and type
            of each animal found in the input data.
    """
    output_data = ""
    for data in animals_data:
        output_data += f'Name: {data.get("name", "Unknown")}\n'
        chars = data.get("characteristics", {})
        if "diet" in chars:
            output_data += f'Diet: {chars["diet"]}\n'
        locs = data.get("locations", [])
        if locs:
            output_data += f'Location: {locs[0]}\n'
        if "type" in chars:
            output_data += f'Type: {chars["type"]}\n'
        output_data += "\n"
    return output_data


animals_data = load_data('animals_data.json')
print(print_data_fox_in_json(animals_data))