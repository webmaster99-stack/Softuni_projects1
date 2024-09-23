# Softuni_projects1
This repository has all projects I have done at school

Interactive Data Type Operations System is a simple software that takes input from the user (a number between 1 and 4) and performs operations depending no the coresponding data type
1. Strings
2. Numbers
3. Booleans
4. Aditional data types(Lists, Tuples, Dictionaries)

Strings - the software declares a variable named sentence and assigns the string value Learning Python is fun, then extracs the word python using string slicing and displays it, then converts the entire string in uppercase letters and displays it.
Numbers - the software asks the user to input two numbers, the it performs basic arithmetic operations with te numbers(addition, subtraction, multiplrcation, division, exponent) and displays the result. I've handled the case of division by zero in case the user inputs zero as the second number
Booleans - the software declares two variables - is_python_fun with a value of True and is_funny with the value of False, then it performs logical operations with and, or and not operators and comparison operators and displays the results
Additional Data Types - the software creates a list, a tuple and a dictionary and performs different modifications depending on the data type. I've handled the type error in the case of modifying a tuple by printing the message 'Tuples are immutable so you cannot modify them in any way'.

I've separeted the logic of the software into two modules - functions_mudule which comtains function definitions for the different operations corresponding to the different data types and main_logic module which takes the user input and performs control flow on it. I've imported functions_module in main_logic module and in the check section called the corresponding function:
if the user's choise is 1 - call functions_module.sting_manipulation() etc. I've handled the case in which the user inputs a different input than the required by printing the message 'Invalid input! Please enter a number between 1 and 4'


Pattern Drawing - pattern drawing programs for different types of patterns, drwawn by using nested for loops

Rock Paper Scissors is a simple game that takes input form the user( r for rock, p for paper and s for scissors), a random number in range 1 to 3 for the computer choice( 1 for rock, 2 for paper and 3 for scissors), then comperes them and depending on the result displays a
message
The rules are as follows:
Rock breaks scissors
Scissors cuts paper
Papper covers rock
If both choices are the same the result is a Draw


Guess The Number is a simple game that takes a random number between 1 and 100 for the computer's choice and a number for the user's input. The game takes the user's input implementing a while loop and compares the two numpers(user input and computer's choice) ard depending on the case displays a message: if the user's input matches the computer's choice the message 'You gueesed it!' is displayed and the game ends, if the user's input is greater than the computer's choice the message 'Too high!' is displayed, if the user's input is smaller than the computer's choice the message 'Too low!' is displayed. I've handled the case in which the user inputs anything different than a number be displaying the message 'Invalid input! Try again..' 
