# Softuni_projects1
This repository has all projects I have done at school
## Interactive Data Type Operations System

Interactive Data Type Operations System is a simple software that takes input from the user (a number between 1 and 4) and performs operations depending on the coresponding data type
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

## Pattern Drawing

Pattern drawing programs for different types of patterns, drwawn by using nested for loops

## Rock Paper Scissors 

Rock Paper Scissors is a simple game that takes input form the user( r for rock, p for paper and s for scissors), a random number in range 1 to 3 for the computer choice( 1 for rock, 2 for paper and 3 for scissors), then comperes them and depending on the result displays a
message
The rules are as follows:
Rock breaks scissors
Scissors cuts paper
Papper covers rock
If both choices are the same the result is a Draw

## Guess The Number

Guess The Number is a simple game that takes a random number between 1 and 100 for the computer's choice and a number for the user's input. The game takes the user's input implementing a while loop and compares the two numpers(user input and computer's choice) and depending on the case displays a message: if the user's input matches the computer's choice the message 'You gueesed it!' is displayed and the game ends, if the user's input is greater than the computer's choice the message 'Too high!' is displayed, if the user's input is smaller than the computer's choice the message 'Too low!' is displayed. I've handled the case in which the user inputs anything different than a number be displaying the message 'Invalid input! Try again..' 

## Bank Account Management System

Bank Account Management System is a program that takes a number between 1 and 10 from the user and performs operations depending on the coresponding number
1. Create an account
2. Deposit
3. Withdraw
4. Check Balance
5. List Accounts
6. Transfer Funds
7. View Transaction History
8. Apply For Loan
9. Repay Loan
10. Exit

Create an account - the software asks the user to input a name and creates an account with that name and appends it to a account_holders list where all accounts are stored, then it creates a variable balance, assigns a value 0 to it and appends it to a list balances where all balancec are stored, then it creates an empty transaction history list and append it to a transaction histories list where all transaction histories are stored, then it creates an outstanding loan variable, assigns a value of 0 to it appends it to a list loans where all loans are stored, then the software displays a message 'Account creation successful'.
Deposit - the software asks the user to input the account holder's name and checks if the name is in the system. If the name is in the system it asks the user to enter a deposit amount, it updates the current account holder's balance and logs the transaction in the current account holder's transaction history and it displays a message with the updated balance. If the name is not i the software informs the user with the message 'Non-existing account!'.
