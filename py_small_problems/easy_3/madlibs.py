

def madlib():
    noun = input('Enter a noun\n').strip()
    verb = input('Enter a verb\n').strip()
    adjective = input('Enter an adjective\n').strip()
    adverb = input('Enter an adverb\n').strip()
    print(f'''
My {adjective} {noun} {verb}s {adverb} over the horizon...
The {adjective} {noun} exclaims his legendary status.
He {adverb} falls off the cliff
''')
    
madlib()