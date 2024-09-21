import random

computer_choice = random.randint(1, 100)
while True:
    player_input = input('Guess the number (1, 100): ')

    if not player_input.isdigit():
        print('Invalid input! Try again...')
        continue

    player_number = int(player_input)
    if player_number == computer_choice:
        print('You guessed it!')
        break
    elif player_number > computer_choice:
        print('Too High!')
    elif player_number < computer_choice:
        print('Too Low!')


