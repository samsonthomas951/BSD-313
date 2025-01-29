class BankAcount:
    def __init__(self,account_number,balance,date_of_openning,account_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_openning = date_of_openning
        self.account_name = account_name

    def deposit(self):
       dep = int(input(print("Enter amount to be deposited: ")))
       return dep
    def withdraw(self):
        amount = int(input(print("Enter amount to be withdrawn: ")))
        if amount> self.balance:
            print("Insuficient balance")
        else:
            print(f"You have withdrawn {amount } from your account.")
    
    def check_balance(self):
        print(f"Your current balance is Ksh. {self.balance}")

    def customer_details(self):
        print(f"Customer Name: {self.account_name}\t Account Number: {self.account_number}\t Date of opening: {self.date_of_openning}\t Balance: {self.balance}")

bank = BankAcount(12312,55000,"Monday, January 27, 2025","AC231CV21")
#depositing 
print(bank.deposit())

bank.withdraw()
bank.check_balance()
bank.customer_details()