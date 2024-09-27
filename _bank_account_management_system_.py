account_holders = []
balances = []
transaction_histories = []
loans = []

max_loan_amount = 10000
interest_rate = 0.03

def create_account():
    name = input('Enter the account holder\'s name: ')
    account_holders.append(name)
    balance = 0.00
    balances.append(balance)
    transactions_history = []
    transaction_histories.append(transactions_history)
    outstanding_loan_amount = 0.00
    loans.append(outstanding_loan_amount)
    print('Account creation successful!')


def deposit():
    """Deposit money into an account"""
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        deposit_amount = float(input('Enter amount to deposit: '))
        balances[account_holders.index(name)] += deposit_amount
        current_transaction = 'deposit: ' + str(deposit_amount)
        transaction_histories[account_holders.index(name)].append(current_transaction)
        print(f'Your current balance is: {balances[account_holders.index(name)]}')
    else:
        print('Non-existing account!')


def withdraw():
    """Withdraw money from an account."""
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        withdraw_amount = float(input('Enter to withdraw: '))
        if balances[account_holders.index(name)] >= withdraw_amount:
            balances[account_holders.index(name)] -= withdraw_amount
            current_transaction = 'withdraw: ' + str(withdraw_amount)
            transaction_histories[account_holders.index(name)].append(current_transaction)
            print(f'Your current balance is: {balances[account_holders.index(name)]}')
        else:
            print('Insufficient funds to complete the operation!')
    else:
        print('Non-existing account!')


def check_balance():
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        print(f'Your current balance is: {balances[account_holders.index(name)]}')
    else:
        print('Non-existing account!')


def list_accounts():
    if len(account_holders) > 0:
        for i in range(len(account_holders)):
            print(account_holders[i])
            print(balances[i])
            print(loans[i])
    else:
        print('Non-existing account!')


def transfer_funds():
    sender_name = input('Enter sender name: ')
    recipient_name = input('Enter recipient name: ')
    if sender_name in account_holders and recipient_name in account_holders:
        transfer_amount = float(input('Enter amount to transfer: '))
        if balances[account_holders.index(sender_name)] >= transfer_amount:
            balances[account_holders.index(sender_name)] -= transfer_amount
            balances[account_holders.index(recipient_name)] += transfer_amount
            current_transfer = 'transfer: ' + str(transfer_amount)
            current_received = 'received: ' + str(transfer_amount)
            transaction_histories[account_holders.index(sender_name)].append(current_transfer)
            transaction_histories[account_holders.index(recipient_name)].append(current_received)
            print('Transfer successful!')
        else:
            print('Insufficient funds to complete the operation!')
    else:
        print('Both or one of the accounts does not exist!')


def view_transactions_history():
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        if len(transaction_histories[account_holders.index(name)]) > 0:
            print(f'Your transaction history: {transaction_histories[account_holders.index(name)]}')
        else:
            print('There are no transactions in your transactions history!')
    else:
        print('Non-existing account!')


def apply_for_loan():
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        index = account_holders.index(name)
        loan_amount = float(input(f'Enter the loan amount(max {max_loan_amount} leva): '))
        if loan_amount <= max_loan_amount:
            balances[index] += loan_amount
            loans[index] += loan_amount * (1 + interest_rate)
            print(f'Loan of {loan_amount:.2f} leva approved for {name}. New balance: {balances[index]:.2f} leva.')
        else:
            print(f'Loan amount exceeds the maximum limit of {max_loan_amount} leva.')
    else:
        print('Non-existing account')


def repay_loan():
    name = input('Enter the account holder\'s name: ')
    if name in account_holders:
        index = account_holders.index(name)
        repayment_amount = float(input(f'Emter repayment amount(Outstanding loan: {loans[index]:.2f} leva): '))
        if repayment_amount <= loans[index]:
            balances[index] -= repayment_amount
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
    choice = int(input('Enter your choice: '))
    return choice


def main():
    while True:
        choice = display_menu()
        if choice == 1:
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
            break
        else:
            print('Invalid choice. Please try again.')


main()














