rows = int(input('Enter the number of rows: '))

for i in range(1, rows + 1):
    for j in range(i - 1):
        print(' ', end='')

    for k in range(2 * (rows - i) + 1):
        print('*', end='')

    print()
