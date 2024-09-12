# importing for computer choice
import random

# setting constants
VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']

# returns a list to display choices with () around short choices
def return_choices_list():
    display_list = []

    for option in VALID_CHOICES:
        if option not in ['scissors', 'spock']:
            short = option[0]
            option = f'({short}){option[1:]}'
        else:
            short = option[0:2]
            option = f'({short}){option[2:]}'

        display_list.append(option)

    return ', '.join(display_list)

# creates a list of valid short choices
def shortened_choices():
    shortened_list = []

    for option in VALID_CHOICES:
        if option not in ['scissors', 'spock']:
            short = option[0]
        else:
            short = option[0:2]

        shortened_list.append(short)

    return shortened_list
# if given a shortened input, converts to full word

def process_shortened_input(short_input):
    for word in VALID_CHOICES:
        if word.startswith(short_input):
            return word

# default print format
def prompt(message):
    print(f'==> {message}')

# checks choice for valid input
def invalid_choice(player_choice):
    return (player_choice.casefold() not in VALID_CHOICES and
            player_choice.casefold() not in valid_shortened_choices)

# computes if player wins
def player_won(player, computer):
    return ((player == 'rock' and (computer in
                                ['scissors', 'lizard'])) or
        (player == 'scissors' and (computer in
                                ['paper', 'lizard'])) or
        (player == 'paper' and (computer in
                                ['rock', 'spock'])) or
        (player == 'lizard' and (computer in
                                ['spock', 'paper'])) or
        (player == 'spock' and (computer in
                                ['scissors', 'rock']))
    )

# checks play_again for valid input
def invalid_again(again_choice):
    return not(again_choice.startswith('n') or again_choice.startswith('y'))

# displays total wins
def display_total_wins():
    print(f'''
You have {player_wins} wins!
The computer has {computer_wins} wins
           ''')

# more variables
display_choices = return_choices_list()
valid_shortened_choices = shortened_choices()

while True:

    # keeps track of best out of 5
    player_wins = 0
    computer_wins = 0

    while True:

        # prompts for a choice and validates input
        prompt(f'Choose one: {display_choices}')
        choice = input()

        while invalid_choice(choice):
            prompt('Please enter a valid choice')
            choice = input()

        if choice in valid_shortened_choices:
            choice = process_shortened_input(choice)

        # computer chooses at random
        computer_choice = random.choice(VALID_CHOICES)

        # displays choices from both sides
        prompt(f'You chose {choice}, computer chose {computer_choice}')

        # displays the winner of the round, keeps track of score
        if player_won(choice, computer_choice):
            prompt('You won this round!')
            player_wins += 1
        elif choice == computer_choice:
            prompt('You tied this round.')
        else:
            prompt('You lost this round :(')
            computer_wins += 1

        # displays total wins at the end of round
        display_total_wins()

        # checks to see if won
        if player_wins == 3:
            prompt('You won the game!')
            break
        if computer_wins == 3:
            prompt('You lost the game :(')
            break

    # asks user to play again and validates input
    prompt('Would you like to play again? (y/n)')
    play_again = input().lower()

    while invalid_again(play_again):
        prompt('Please enter a valid choice (y/n)')
        play_again = input().lower()

    if play_again[0].lower() == 'n':
        break

    print('--------------------------------------')