# write a function that takes two strings as arguments
# creates a longer and shorter string variable
# compares the length of the two strings
    # assigns accordingly
# returns shorter + longer + shorter

def short_long_short(str1, str2):
    short = ""
    long = ""
    if len(str1) > len(str2):
        long = str1
        short = str2
    else:
        long = str2
        short = str1
    return (short + long + short)

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")