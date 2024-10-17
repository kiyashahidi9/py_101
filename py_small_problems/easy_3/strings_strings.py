# def stringy with a num argument
# assign the variable base to the value '10' times num //2
# if the number is even, return base
# if the number is odd, return '{base}1'

def stringy(num):
    base = '10' * (num // 2)
    if num % 2 == 0:
        return base
    else:
        return f'{base}1'
    
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True