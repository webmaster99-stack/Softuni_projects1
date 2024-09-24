import random
computer_choice = random.randint(1, 100)
difficulty_level = input('Enter a difficulty level between 1 and 3: ')
count_attempts = 0
number_range = 0

if difficulty_level == '1':
   count_attempts = 20
   number_range = range(1, 101)
   print(f'You will have {count_attempts} attempts to guess the number')
elif difficulty_level == '2':
    count_attempts = 10
    number_range = range(1, 201)
    print(f'You will have {count_attempts} attempts to guess the number')
elif difficulty_level == '3':
    count_attempts = 5
    number_range = range(1, 301)
    print(f'You will have {count_attempts} attempts to guess the number')
else:
    print('Invalid input!Try again...')

for _ in range(count_attempts):
    player_input = input(f'Guess the number {number_range}: ')

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
else:
    print('Sorry you ran out of attempts')
