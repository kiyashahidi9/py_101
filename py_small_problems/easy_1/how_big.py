# Prompts for measurement, checks if valid, repeats if not
while True:
    measurement = input('Do you prefer feet or meters: (f/m) ')
    if measurement == 'f' or measurement == 'm':
        break

    print('\nPlease put a valid measurement (f/m) ')

# Prompts for length and width, Calculates area
length = float(input('What is the length of the room?: '))
width = float(input('What is the width of the room?: '))
area = length * width

# Determines which output, depending on measurement preference
# Displays the conversion of alternative measurement
if measurement == 'f':
    print(f'The area of the room is {area:.2f} sq. feet.'
          f' ({area/10.7639:.2f} sq. meters.)')
else:
    print(f'The area of the room is {area:.2f} sq. meters.'
          f' ({area * 10.7639:.2f} sq. feet.)')
