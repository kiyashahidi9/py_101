import json

with open('valid_colors.json', 'r') as file:
    VALID = json.load(file)

def is_color_valid(color):
    return color.casefold() in VALID['valid_colors']

input_color = input('Enter a color\n')

print(is_color_valid(input_color))