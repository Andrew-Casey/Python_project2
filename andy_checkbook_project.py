import os
from datetime import datetime 
# define the file paths for account balance and transaction history
ACCOUNT_FILE = "account.txt"
HISTORY_FILE = "history.txt"

# check if the file exists and create a new file with initial balance of 0 if it doesn't exist
if not os.path.exists(ACCOUNT_FILE):
    with open(ACCOUNT_FILE, 'w') as g:
        g.write("0.00")

if not os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, 'w') as h:
        h.write("0.00" + '\n')

# define the function for each action
def view_balance():
    with open(ACCOUNT_FILE, 'r') as g:
        balance = float(g.read())
    print(f"Your current balance is: ${balance:.2f}")

def check_history():
    with open(HISTORY_FILE, 'r') as h:
        history = h.read().strip()
    if not history:
        print("Your transaction history is empty.")  
    else:
        history_list = history.split("\n")
        for i, amount in enumerate((history_list)):
            print(f"{i+1}. ${amount}\n")

def add_debit():
    amount = input("Enter the amount to withdraw: ")
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        return
    with open(ACCOUNT_FILE, 'r') as g:
        balance = float(g.read())
    if amount > balance:
        print("Insufficient balance.")
        return
    with open(ACCOUNT_FILE, 'w') as g:
        balance -= amount
        g.write(f"{balance:.2f}")
    with open(HISTORY_FILE, 'a') as h:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        h.write(f"-{amount:.2f} Withdrawal on {dt_string}\n")
    print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")

def add_credit():
    amount = input("Enter the amount to deposit: ")
    try:
        amount = float(amount)
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive number.")
        return
    with open(ACCOUNT_FILE, 'r') as g:
        balance = float(g.read())
    with open(ACCOUNT_FILE, 'w') as g:
        balance += amount
        g.write(f"{balance:.2f}")
    with open(HISTORY_FILE, 'a') as h:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        h.write(f"{amount:.2f} Deposit on {dt_string}\n")

    print(f"Deposit successful. Your new balance is: ${balance:.2f}")

# loop until the user chooses to exit
while True:
    print("\nWelcome to the banking app!")
    print("What would you like to do?")
    print("1. View current balance?")
    print("2. Withdraw funds")
    print("3. Deposit funds")
    print("4. Check transaction history")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_balance()
    elif choice == '2':
        add_debit()
    elif choice == '3':
        add_credit()
    elif choice == '4':
        check_history()
    elif choice == '5':  
        print("Thank you for using the banking app.")
        break
    else:
        print("Invalid choice. Please try again.")
