from datetime import datetime

age = int(input('What is your age?\n'))

retire_age = int(input('At what age would you like to retire?\n'))

year = datetime.now().year

print(f"It's {year}. You will retire in {year + retire_age}")
print(f'You have only {retire_age - age} years of work to go!')