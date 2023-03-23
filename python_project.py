import os

##check if the file exists
if not os.path.exists('account.txt'):
#create a new file with initial balance of 0
    with open('account.txt','w')as f:
        f.write('0.00')
        
#Define the function for each action
def view_balance():
    with open('account.txt','r') as f:
        balance = float(f.read())
    print('Your current balance is: ', balance)

def add_debit(): #withdrawal
    amount = input('Enter the amount to withdraw: ')
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        print('Invalid input. Pleases enter a positive number.')
        add_debit()
        return
    with open('account.txt','r') as f:
        balance = float(f.read())
    if amount > balance:
        print('Insufficient balance.')
        return
    balance -= amount
    with open('account.txt','w') as f:
        f.write(str(balance))
    print('Withdrawal successful. Your new balance is: ', balance)   

def add_credit(): #deposit
    amount = input('Enter the amount to deposit: ')
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        print('Invalid input. Please enter a positive number.')
        add_credit()
        return
    with open('account.txt','r') as f:
        balance = float(f.read())
    balance += amount
    with open('account.txt','w') as f:
        f.write(str(balance))
    print('Deposit successful. Your new balance is: ', balance)
        
#loop until the user chooses to exit
while True:
        print('\nWelcome to the banking app!')
        print('What would you like to do?')
        print('1. View current balance?')
        print('2. Add a debit (withdrawal)')
        print('3. Add a credit (deposit)')
        print('4. Exit')
        choice =input('Enter your choice: ')
        if choice == '1':
            view_balance()
        elif choice == '2':
            add_debit()
        elif choice == '3':
            add_credit()
        elif choice == '4':
            print('Thank you for using the banking app')
            break
        else:
            print('invalid choice. Please Try again.')
        
