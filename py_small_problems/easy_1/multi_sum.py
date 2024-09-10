# write a function
# initialize a list
# iterate through the range of 1 to the input number
# if they are a multiple of 3 or 5, add to list
# the result is the sum of all the numbers in the list

def is_multiple(num, div):
    return num % div == 0

def multisum(num):
    result = 0
    for i in range(1, num + 1):
        if is_multiple(i, 3) or is_multiple(i, 5):
            result += i
    return result

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)