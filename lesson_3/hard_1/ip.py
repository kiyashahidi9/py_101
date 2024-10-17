# now we have each number
# figure out if each number is an ip number
# if the len of list is 4

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return number in range(0, 256)
    return False

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    counter = 0
    while counter < len(dot_separated_words):
        word = dot_separated_words[counter]
        if not is_an_ip_number(word):
            return False
        
        counter += 1

    return len(dot_separated_words) == 4


print(is_dot_separated_ip_address('10.4.5.34'))