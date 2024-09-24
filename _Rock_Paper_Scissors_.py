import random
from colorama import Fore
rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

counter_win = 0
counter_draw = 0
counter_lose = 0
counter_first_input = 0

while True:
    player_move = input(Fore.BLACK + 'Choose [r]ock, [p]aper or [s]cissors: ' + Fore.GREEN)

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid input! Try again...')
        continue
    counter_first_input += 1

    computer_move = ''
    computer_random_number = random.randint(1, 3)

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors
    print(Fore.BLUE + f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or\
        (player_move == paper and computer_move == rock) or\
        (player_move == scissors and computer_move == paper):
        result = 'w'
        counter_win += 1
        print(Fore.GREEN + 'You win this round!')
    elif player_move == computer_move:
        result = 'd'
        counter_draw += 1
        print(Fore.YELLOW + 'It\'s a Draw!')
    elif (player_move == rock and computer_move == paper) or\
        (player_move == paper and computer_move == scissors) or\
        (player_move == scissors and computer_move == rock):
        result = 'l'
        counter_lose += 1
        print(Fore.RED + 'You lose this round!')
    print(Fore.BLACK + f'Current score after the game {counter_first_input}/3: '
          f'[Wins: {counter_win}] [Draws: {counter_draw}] [Losses: {counter_lose}]')
    if counter_first_input == 3:
        break
print('\n--- Final Result ---')
if counter_win > counter_lose:
    success_rate = (counter_win / 3) * 100
    print(Fore.GREEN + f'Congratulations! You won the series with a success rate of {success_rate:.2f}%')
elif counter_win == counter_lose:
    print(Fore.YELLOW + 'The series ends in a draw')
else:
    success_rate = (counter_win / 3) * 100
    print(Fore.RED + f'Sorry, you lost the series. Your success rate was {success_rate:.2f}%. Try again')



