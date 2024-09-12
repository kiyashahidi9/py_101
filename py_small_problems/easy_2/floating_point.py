# define a function to return a ==> in front of each message
# ask user for two positive float numbers(num1 and num2)
# print every operation between num1 and num2 in an fstring

def p(message):
    return f'==> {message}'

num1 = float(input(p('Enter the first number:\n')))
num2 = float(input(p('Enter the second number:\n')))

print(p(f'{num1} + {num2} = {num1 + num2}'))
print(p(f'{num1} - {num2} = {num1 - num2}'))
print(p(f'{num1} * {num2} = {num1 * num2}'))
print(p(f'{num1} / {num2} = {num1 / num2}'))
print(p(f'{num1} // {num2} = {num1 // num2}'))
print(p(f'{num1} % {num2} = {num1 % num2}'))
print(p(f'{num1} ** {num2} = {num1 ** num2}'))