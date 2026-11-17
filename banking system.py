'''
"Workfallow"
"banking system" is a simple structure of banking system which is used to manage the bank accounts and transactions. it allows users to create accounts, deposit and withdraw money, and view account balances.

cases:
A. user creates an account.
B. user deposits money.
C. user withdraws money.
D. user sees the remaining balance of account.
E. user exit from service
'''
print("welocome to python banking")

def create_account():
    name = input("enter your name: ")
    print("account created successfully")
    

balance = 2000

def deposit():
    global balance
    amount = float(input("enter the amount to deposit:"))
    if amount >0:
        balance += amount
        print("deposit successful")
    else:
        print("invalid amount")
    return balance

def withdraw():
    global balance
    amount = float(input("enter the amount to withdraw:"))
    if amount >0 and amount <=balance:
        balance -= amount
        print("withdraw successfull")
    else:
        print("invalid amount or insufficient balance")
    return balance


def check_balance():
    print("your remaining balance is:",balance)
    
while True:
    print("1. create account")
    print("2. deposit money")
    print("3. withdraw money")
    print("4. check balance")
    print("5. exit")
    
    choice = input("enter your choice:")
    if choice == '1':
        create_account()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        check_balance()
    elif choice == '5':
        print("thanks for using service")
        break
    else: 
        print("invalde choice")



