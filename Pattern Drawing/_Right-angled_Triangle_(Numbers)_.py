rows = int(input('Enter the number of rows: '))

for row in range(0, rows + 1):
    for col in range(row + 1):
        print(col + 1, end=' ')
    print()
