size = int(input('Enter rhe size of the square'))
for i in range(size):
    for j in range(size):
        # print * completely in first and last row
        # print * only in first and last position in other rows
        if i == 0 or i == size - 1 or j == 0 or j == size - 1: # Ако сме на първия или на послрдния ред еле ако сме на първата или последната колона- принтираме '*'
            print('*', end='')
        else: # Иначе - принтираме ' '
            print(' ', end='')
    print()