def menu():
    print('Choose a data type to perform operations on: ')
    print('1. Strings')
    print('2. Numbers')
    print('3. Booleans')
    print('4. Additional data types (List, Tuple, Dictionary )')


def string_manipulation():
    print('You choose strings')
    my_string = ' ,no doubt!'
    sentence = 'Learning Python is fun'
    print(sentence + my_string)
    print(sentence[9:15])
    print(sentence.upper())
    print(sentence.replace('fun','awesome'))


def number_manipulation():
    print('You choose numbers')
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter a second number: '))
    print(f'Addition: {num1} + {num2} = {num1 + num2}')
    print(f'Subtraction: {num1} - {num2} = {num1 - num2}')
    print(f'Multiplication: {num1} * {num2} = {num1 * num2}')
    if num2 == 0:
        try:
            print(f'Division: {num1} / {num2} = {num1 / num2}')
        except ZeroDivisionError:
            print('Cannot divide any number by zero')
    else:
        print(f'Division: {num1} / {num2} = {num1 / num2}')
        print(f'Calculating reminder: {num1} % {num2} = {num1 % num2}')
    print(f'{num1} raised to the power of {num2} is: {num1 ** num2}')


def boolean_manipulation():
    print('You choose booleans')
    is_python_fun = True
    is_funny = False
    print(f'The result of {is_python_fun} and {is_funny} is: {is_python_fun and is_funny}')
    print(f'The result of {is_python_fun} or {is_funny} is: {is_python_fun or is_funny}')
    print(f'The result of not {is_python_fun} is: {not is_python_fun}')
    print(f'The result of not {is_funny} is: {not is_funny}')
    print(f'The result of {10 > 5} and {5 == 5} is: {10 > 5 == 5}')


def additional_data_types_manipulation():
    print('Lists')
    print('Creating a list: [1, 2, 3, "Python", True]')
    my_list = [1, 2, 3, "Python", True]
    print(f'Accessing the forth element of the list: {my_list[3]}')
    print('Tuples')
    print('Creating a tuple: ("apple", "banana", "cherry")')
    my_tuple = ("apple", "banana", "cherry")
    print(f'The lenght of the tuple is: {len(my_tuple)}')
    print('Attempting modification of the tuple')
    try:
        my_tuple[2] = 'strawberry'
    except TypeError:
        print('Tuples are immutable so you cannot modify them i any way')
    print('Dictionaries')
    print('Creating a dictionary:')
    my_dictionary = {"name": "Alice", "age": 25, "city": "New York"}
    print(f'Accessing the value of the key age: {my_dictionary['age']}')
    print('Adding a new key:value pair country and USA: ')
    print(f'Old dictionary: {my_dictionary}')
    my_dictionary['country'] = 'USA'
    print(f'Updated dictionary: {my_dictionary}')



