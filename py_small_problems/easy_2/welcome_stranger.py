# write a function greetings that takes two arguments(list, key)
# write a name variable and set it to list joined with spaces
# write a occupation variable and set it to the title and occupation keys
# return appropriate string

def greetings(name_list, key):
    name = ' '.join(name_list)
    occupation = f'{key['title']} {key['occupation']}'
    return f'Hello, {name}! Nice to have a {occupation} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)