# set a variable name to input 
# determine if the name[-1] == '!'
# if so, print out the yelling template
# if else, print out the normal template

name = input('What is your name?\n')
if name[-1] == '!':
    print(f'HELLO {name.upper()} WHY ARE WE YELLING?')
else:
    print(f'Hello {name.title()}.')