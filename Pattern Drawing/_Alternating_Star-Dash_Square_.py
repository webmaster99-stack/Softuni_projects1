size = int(input('Enter the size of th shape: '))

for i in range(size):
    for j in range(size):
        if i % 2 != 0:
            if j % 2 != 0:
                print('*', end='')
            else:
                print('_', end='')

        else:
            if j % 2 != 0:
                print('_', end='')
            else:
                print('*', end='')
    print()
