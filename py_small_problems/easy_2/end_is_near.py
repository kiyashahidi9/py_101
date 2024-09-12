# checking for numbers
def invalid_sentence_numbers(input):
    return input.isnumeric()

# checking for one or no words
def invalid_sentence_one_word(input):
    return len(input.split()) <= 1

# validating sentence input
def invalid_sentence(input):
    return (invalid_sentence_one_word(input) or 
            invalid_sentence_numbers(input))
    
# validating preference input
def invalid_preference(input):
    return (input not in ['p', 'm'])

# computing penultimate word
def penultimate(words):
    word_list = words.split()
    return word_list[-2]

# computing middle world
def middle(words):
    word_list = words.split()
    return word_list[len(word_list) // 2]

# gathers sentence and validates it
sentence = input('Please enter a sentence with more than one word\n')
while invalid_sentence(sentence):
    sentence = input('Please enter a valid sentence\n')

# gathers preference and validates it
return_preference = input('Would you like to get the penultimate (p)' 
                          ' or the middle (m) word?\n')
while invalid_preference(return_preference):
    return_preference = input('Please enter a valid input\n')

# does the operation according to preference
match return_preference:
    case 'p':
        result = penultimate(sentence)
        preference = 'penultimate'
    case 'm':
        result = middle(sentence)
        preference = 'middle'

# displays result
print(f'The {preference} word is: {result}')
