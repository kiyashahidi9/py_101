start = int(input('Which odd number to start?: '))
end = int(input('Which odd number to end?: '))

def check_even(num):
    return num % 2 == 0

for num in range(start, end + 1, 2):
    if check_even(start) or check_even(end):
        print('please enter an odd number!')
        break
    print(num)