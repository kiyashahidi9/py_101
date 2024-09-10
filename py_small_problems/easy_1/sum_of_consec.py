# defining functions
def compute_sum(target):
    return sum(range(1, target + 1))

def compute_product(target):
    result = 1
    for num in range(1, target + 1):
        result *= num
    return result

# asks user for integer input and checks if valid
num = input('Please enter an integer greater than 0\n')
while True:
    try:
        int(num)
    except ValueError:
        num = input('Please enter a valid number\n')
    else:
        if int(num)> 0:
            break
        else:
            num = input('Please enter a number greater than zero\n')
num = int(num)

# asks user for operation and checks if valid
# performs operation
op = input('Enter "s" to computer the sum, or "p" to compute the product\n')
while True:
    match op:
        case 's':
            op_code = "sum"
            result = compute_sum(num)
            break
        case 'p':
            op_code = 'product'
            result = compute_product(num)
            break
        case _:
            op = input('Please enter (p/s)\n')

# displays result
print(f'The {op_code} of the integers between 1 and {num} is {result}')