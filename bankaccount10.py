class BankAccount:

  
    def __init__(self, account_number, account_holder, account_type):
        self.account_number = account_number
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = 0

  
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

   
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid amount.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    
    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Number :", self.account_number)
        print("Account Holder :", self.account_holder)
        print("Account Type   :", self.account_type)
        print("Current Balance:", self.balance)



account_number = input("Enter account number: ")
account_holder = input("Enter account holder name: ")
account_type = input("Enter account type: ")


account1 = BankAccount(account_number, account_holder, account_type)


deposit_amount = float(input("Enter amount to deposit: "))
account1.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
account1.withdraw(withdraw_amount)


account1.display_details()