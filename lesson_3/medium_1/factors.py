def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

input_num = int(input('Input a number\n'))

print(factors(input_num))