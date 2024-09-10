number = int(input('Is it odd?: '))

def is_odd(integer):
    return abs(integer) % 2 == 1

print(is_odd(number))