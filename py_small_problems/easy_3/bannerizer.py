# def print_in_box(str)
# initialize variable box_len and set it to len(str) + 4

def print_in_box(str):
    box_len = len(str) + 6
    box_edge = f'+{'-' * box_len}+'
    box_close = f'|{" " * box_len}|'
    box_middle = f'|{str.center(box_len)}|'
    print(box_edge)
    print(box_close)
    print(box_middle)
    print(box_close)
    print(box_edge)

print_in_box('To boldly go where no one has gone before.')
print_in_box('')