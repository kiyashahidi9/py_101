# def function center_off(str)
# initialize variable: str_length = len(str)
# initialize variable: middle_char = str_length/2
# if str_length % 2 == 0:
# return str[middle_char: middle_char + 1]
# else:
# return str[middle_char]

def center_of(str):
    str_length = len(str)
    middle_char = str_length // 2
    if str_length % 2 == 0:
        return str[middle_char - 1: middle_char + 1]
    else:
        return str[middle_char]
    
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True