# def triangle(n)
# assign variable width to n
# for i in range(1, n+1)
# print(f'{' ' * width}{'*' * i}')

def triangle(n):
    width = n
    for i in range(1, n + 1):
        print(f'{' ' * width}{'*' * i}')
        width -= 1

triangle(9)
