import json


def json_load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def create_animal_data_text(animals_data):
    """
        Parses a list of animal data dictionaries and formats it into a readable string.
        Input: json (list[dict])
        Returns:
        str: A formatted string containing the name, diet, first location, and type
            of each animal found in the input data.
    """
    output_data = ""
    for data in animals_data:
        output_data += '<li class="cards__item">'
        output_data += f'Name: {data.get("name", "Unknown")}<br/>\n'
        chars = data.get("characteristics", {})
        if "diet" in chars:
            output_data += f'Diet: {chars["diet"]}<br/>\n'
        locs = data.get("locations", [])
        if locs:
            output_data += f'Location: {locs[0]}<br/>\n'
        if "type" in chars:
            output_data += f'Type: {chars["type"]}<br/>\n'
        output_data += "</li>"
    return output_data


def website_load_data(file_path):
    """ Loads the HTML Text """
    with open(file_path, "r", encoding="utf-8") as handle:
        html_data = handle.read()
        return html_data


def replace_marker_with_data(website_text_data, formatted_animal_text):
    """ Substitutes the specified placeholder with its formatted string equivalent. """
    new_website_text = website_text_data.replace("__REPLACE_ANIMALS_INFO__", formatted_animal_text)
    return new_website_text


def created_new_html_data(new_website_text_data):
    """ Writes a new HTML file and fills it with content"""
    with open("animals.html", "w") as handle:
        handle.write(new_website_text_data)


animals_data = json_load_data('animals_data.json')
formatted_animal_text = create_animal_data_text(animals_data)
website_text_data = website_load_data('animals_template.html')
new_website_text_data = replace_marker_with_data(website_text_data, formatted_animal_text)
created_new_html_data(new_website_text_data)