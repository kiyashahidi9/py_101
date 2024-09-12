LANGUAGE = 'en'
import json

# import messages from a config file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

# defining functions
def prompt(message):
    return f'==> {message}'

def invalid_number(num):
    try:
        float(num)
    except ValueError:
        return True
    return False

def calc_stop(again):
    while True:
        match again.casefold():
            case 'y':
                return False
            case 'n':
                return True
            case _:
                again = input(messages('invalid_again'))

def messages(message, lang=LANGUAGE):
    return MESSAGES[lang][message]

# welcomes user
print(prompt(messages('welcome', 'es')))

# allows the user to enter as many calculations as they want
while True:

# ask user for first number and checks if valid
    num1 = input(prompt(messages('first')))

    while invalid_number(num1):
        num1 = input((prompt(messages('invalid_number'))))

    # ask user for second number and checks if valid
    num2 = input(prompt(messages('second')))

    while invalid_number(num2):
        num2 = input(prompt(messages('invalid_number')))

    # ask user for operation and checks if valid
    operation = input(prompt(messages('operation')))

    while operation not in ['1', '2', '3', '4']:
        operation = input(prompt(messages('invalid_operation')))

    # performs operation
    match int(operation):
        case 1:
            output = float(num1) + float(num2)
        case 2:
            output = float(num1) - float(num2)
        case 3:
            output = float(num1) * float(num2)
        case 4:
            output = float(num1) / float(num2)

    # displays result
    print(messages('result').format(output=output))

    # asks user if they wanna do it again
    again = calc_stop(input(messages('again')))

    if again:
        break
