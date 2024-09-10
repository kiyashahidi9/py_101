# ask the user for the first number.
# ask the user for the second number.
# ask the user for an operation to perform
# perform the operation on the to numbers
# print the result to the terminal

# defining functions
def prompt(message):
    return f'==> {message}'

def invalid_number(num):
    try:
        int(num)
    except ValueError:
        return True
    return False

# welcomes user
print(prompt('Welcome to Calculator!'))

# ask user for first number and checks if valid
num1 = input(prompt('What\'s the first number?\n'))

while invalid_number(num1):
    num1 = input((prompt('Hmm... that doesn\'t look like a valid number.'
                         ' Try again\n')))

# ask user for second number and checks if valid
num2 = input(prompt("What's the second number?\n"))

while invalid_number(num2):
    num2 = input(prompt('Hmm... that doesn\'t look like a valid number.'
                        ' Try again\n'))

# ask user for operation and checks if valid
operation = input(prompt('What operation would you like to perform?\n'
                             '1) Add 2) Subtract 3) Multiply 4) Divide\n'))

while operation not in ['1', '2', '3', '4']:
    operation = input(prompt('You must choose 1, 2, 3, or 4\n'))

# performs operation
match int(operation):
    case 1:
        output = int(num1) + int(num2)
    case 2:
        output = int(num1) - int(num2)
    case 3:
        output = int(num1) * int(num2)
    case 4:
        output = int(num1) / int(num2)

# displays result
print(f'The result is: {output}')