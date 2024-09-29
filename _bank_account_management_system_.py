# Initialize lists to hold account data
account_holders = [] # List to store account holder names
balances = []  # List to store corresponding balances
transaction_histories = []  # List to store transaction histories
loans = [] # List to store outstanding loans for each account

max_loan_amount = 10000 # Maximum loan amount
interest_rate = 0.03 # Maximum loan amount

def create_account():
    name = input('Enter the account holder\'s name: ') # Prompts the user for the account holder's name.
    account_holders.append(name)  # Adds the new account holder to the list of account holders.
    balance = 0.00 # Initializes the balance to 0 for the new account.
    balances.append(balance) # Appends the current balance to the balances list
    transactions_history = [] # Initializes an empty transaction history for the new account.
    transaction_histories.append(transactions_history) # Appends the current transaction history to the transaction histories list
    outstanding_loan_amount = 0.00 # Initializes the outstanding loan amount to 0.
    loans.append(outstanding_loan_amount) # Appends the current outstanding loan amount to the loans list
    print('Account creation successful!') # Notifies the user of the successful account creation.


def deposit():
    name = input('Enter the account holder\'s name: ')  # Prompts the user for the account holder's name.
    if name in account_holders: # Checks if the account exists in the system.
        deposit_amount = float(input('Enter amount to deposit: ')) # If the account exists, prompts the user for the amount to deposit.
        balances[account_holders.index(name)] += deposit_amount # Updates the account's balance with the deposited amount.
        current_transaction = 'deposit: ' + str(deposit_amount) # Logs the transaction in the account's transaction history.
        transaction_histories[account_holders.index(name)].append(current_transaction)
        print(f'Your current balance is: {balances[account_holders.index(name)]}') # Displays the updated balance to the user.
    else: # If the account does not exist, informs the user.
        print('Non-existing account!')


def withdraw():
    name = input('Enter the account holder\'s name: ') # Prompts the user for the account holder's name.
    if name in account_holders: # Checks if the account exists in the system.
        withdraw_amount = float(input('Enter to withdraw: ')) # If the account exists, prompts the user for the amount to withdraw.
        if balances[account_holders.index(name)] >= withdraw_amount: # Checks if there are sufficient funds for the withdrawal.
            balances[account_holders.index(name)] -= withdraw_amount # If funds are sufficient, updates the balance and logs the transaction.
            current_transaction = 'withdraw: ' + str(withdraw_amount)
            transaction_histories[account_holders.index(name)].append(current_transaction)
            print(f'Your current balance is: {balances[account_holders.index(name)]}') # Displays the updated balance to the user.
        else:
            print('Insufficient funds to complete the operation!') # If insufficient funds, informs the user.
    else:
        print('Non-existing account!') # If the account does not exist, informs the user.


def check_balance():
    name = input('Enter the account holder\'s name: ') # Prompts the user for the account holder's name.
    if name in account_holders: # Checks if the account exists in the system.
        print(f'Your current balance is: {balances[account_holders.index(name)]}') # If the account exists, displays the current balance.
    else: # If the account does not exist, informs the user.
        print('Non-existing account!')


def list_accounts():
    if len(account_holders) > 0: # Checks if there are any accounts in the system.
        for i in range(len(account_holders)): # If there are accounts, loops through each account holder.
            print(account_holders[i]) # Displays the account holder's name, balance, and outstanding loan amount.
            print(balances[i])
            print(loans[i])
    else: # If there are no accounts, informs the user.
        print('There are no accounts in the system!')


def transfer_funds():
    sender_name = input('Enter sender name: ') # Prompts the user for the sender's and recipient's account holder names.
    recipient_name = input('Enter recipient name: ')
    if sender_name in account_holders and recipient_name in account_holders: # Checks if both accounts exist in the system.
        transfer_amount = float(input('Enter amount to transfer: ')) # If both accounts exist, prompts the user for the amount to transfer.
        if balances[account_holders.index(sender_name)] >= transfer_amount: # Checks if the sender has sufficient funds for the transfer
            balances[account_holders.index(sender_name)] -= transfer_amount # If funds are sufficient, updates both balances and logs the transactions.
            balances[account_holders.index(recipient_name)] += transfer_amount
            current_transfer = 'transfer: ' + str(transfer_amount)
            current_received = 'received: ' + str(transfer_amount)
            transaction_histories[account_holders.index(sender_name)].append(current_transfer)
            transaction_histories[account_holders.index(recipient_name)].append(current_received)
            print('Transfer successful!') # Informs the user of the successful transfer.
        else:
            print('Insufficient funds to complete the operation!')  # If insufficient funds or if either account does not exist, informs the user.
    else:
        print('Both or one of the accounts does not exist!')


def view_transactions_history():
    name = input('Enter the account holder\'s name: ') # Prompts the user for the account holder's name.
    if name in account_holders: # Checks if the account exists in the system.
        if len(transaction_histories[account_holders.index(name)]) > 0: # If the account exists, displays the transaction history.
            print(f'Your transaction history: {transaction_histories[account_holders.index(name)]}')
        else: # If there are no transactions, informs the user.
            print('There are no transactions in your transactions history!')
    else:
        print('Non-existing account!') # If the account does not exist, informs the user.


def apply_for_loan():
    name = input('Enter the account holder\'s name: ')
    if name in account_holders: # Checks if the account exists in the system
        index = account_holders.index(name) # Finds the account index
        loan_amount = float(input(f'Enter the loan amount(max {max_loan_amount} leva): ')) # Prompts user for the loan amount they wish to apply for
        if loan_amount <= max_loan_amount: # Checks if the loan amount is within the limit
            balances[index] += loan_amount # Updates balance and loan amount
            loans[index] += loan_amount * (1 + interest_rate) # Calculates total loan with interest
            print(f'Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.')
        else:
            print(f'Loan amount exceeds the maximum limit of {max_loan_amount} leva.')
    else:
        print('Non-existing account')


def repay_loan():
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        index = account_holders.index(name)
        repayment_amount = float(input(f'Enter repayment amount(Outstanding loan: {loans[index]:.2f} leva): '))# Prompts user for repayment amount
        if repayment_amount <= loans[index]: # Checks if the repayment amount is valid
            balances[index] -= repayment_amount # Updates balance and outstanding loan amount
            loans[index] -= repayment_amount
            print(f'Repayment of {repayment_amount:.2f} leva accepted for {name}. Remaining loan {loans[index]:.2f} leva.')
        else:
            print(f'Repayment amount exceeds outstanding loan.')
    else:
        print('Non-existing account!')


def display_menu():
    print('\n--- Bank Account Management System ---')
    print('1. Create an account')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Check Balance')
    print('5. List Accounts')
    print('6. Transfer Funds')
    print('7. View Transaction History')
    print('8. Apply For Loan')
    print('9. Repay Loan')
    print('10. Exit')
    choice = int(input('Enter your choice: ')) # Prompts user for their choice
    return choice


def main():
    while True:
        choice = display_menu() # Displays the menu and gets user choice
        if choice == 1: # Process user input based on their choice
            create_account()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            check_balance()
        elif choice == 5:
            list_accounts()
        elif choice == 6:
            transfer_funds()
        elif choice == 7:
            view_transactions_history()
        elif choice == 8:
            apply_for_loan()
        elif choice == 9:
            repay_loan()
        elif choice == 10:
            print('Exiting the system. Goodbye!')
            break # Exits the loop and terminates the program
        else:
            print('Invalid choice. Please try again.')


main()














