import random

name = input('Enter a name\n')

if name.strip() == '':
    name = 'teddy'
    
age = random.randint(20,101)

print(f'{name.title()} is {age} years old!')