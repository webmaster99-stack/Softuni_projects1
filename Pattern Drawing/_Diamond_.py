height = int(input('Enter the height of the diamond: '))

for i in range(height):
    for j in range(height - i - 1):
        print(' ', end='')
    for j in range(2 * i + 1):
        print('*', end='')
    print()

for i in range(height - 1):
    for j in range(i + 1):
        print(' ', end='')
    for j in range(2*(height - i - 1) - 1):
        print('*', end='')
    print()