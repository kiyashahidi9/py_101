try:
    num = int(input('Enter a number: '))

    result = 10/num
except ValueError:
    print('invalid input. please enter a valid number')
except ZeroDivisionError:
    print('cannot divide by zero bro')
else:
    print(f'result: {result}')
finally:
    print('exception handling complete. Out!')