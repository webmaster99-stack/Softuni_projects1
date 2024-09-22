import functions_module

functions_module.menu()
choice = input('Enter a number between 1 and 4: ')

if choice == '1':
    functions_module.string_manipulation()
elif choice == '2':
    functions_module.number_manipulation()
elif choice == '3':
    functions_module.boolean_manipulation()
elif choice == '4':
    functions_module.additional_data_types_manipulation()
else:
    print('Invalid input! Please enter a number between 1 and 4')

