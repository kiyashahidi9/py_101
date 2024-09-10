def lower_first(word):
    try:
        return f'{word[0].lower()}{word[1:]}' 
    except (TypeError, IndexError, ValueError):
        return 'Please enter a valid word'
    
word = "Helloo"
print(lower_first(word))