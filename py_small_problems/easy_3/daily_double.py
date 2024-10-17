# make the word into a list
# iterate through the list
# add first index of each item
# return the list joined

def crunch(str):
    crunched_text = ''
    index = 0
    for char in str:
        if len(str) - 1 == index or str[index] != str[index + 1]:
            crunched_text += char

        index += 1
    return crunched_text

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')

# These examples should all print True
