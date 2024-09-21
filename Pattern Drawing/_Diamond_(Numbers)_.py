rows = int(input('Enter number of rows'))

for i in range(rows - 1):
    num = 1
    for j in range(i, rows):
        print(' ', end='')

    for j in range(i):
        print(num, end='')
        num += 1

    for j in range(i+1):
        print(num, end='')
        num -= 1

    print()

for i in range(rows):
    num = 1
    for j in range(i + 1):
        print(' ', end='')

    for j in range(i, rows -1):
        print(num, end='')
        num += 1

    for j in range(i, rows):
        print(num, end='')
        num -= 1

    print()