class Banking_system:

    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.balance=0

    def login(self,username,password):
        if self.username==username and self.password==password:
            return True
        else:
            return False

    def deposit(self,amount):
        self.balance += amount
        print("Deposited amount is Rs.",amount,"New balance:",self.balance)

    def withdrawal(self,amount):
        if self.balance > amount:
          self.balance -= amount
          print("Withdrawn amount is Rs.", amount, "New balance:", self.balance)
        else:
            print("Insufficient balance")

account=Banking_system("Parvathy94","Parvathy1994")
def account_login():
    username=input("Enter your username:")
    password=input("Enter your password:")
    if account.login(username,password):
        print("***Login successful***")
        return True
    else:
        print("Invalid username or password")
        return False

def deposit_funds():
    amount=float(input("Enter the amount to deposit:"))
    account.deposit(amount)

def withdraw_funds():
    amount=float(input("Enter the amount to withdraw:"))
    account.withdrawal(amount)

def main():
    while True:
       print("Welcome to Banking system")
       print("1. Account login")
       print("2. Deposit funds")
       print("3. Withdraw funds")
       print("4. Exit")
       choice = int(input("Enter your choice (1-4):"))

       if choice == 1:
           account_login()
       elif choice == 2:
           if account_login():
               deposit_funds()
       elif choice == 3:
           if account_login():
               withdraw_funds()
       elif choice == 4:
           print("Exit")
           break;
       else:
           print("Invalid choice.Please try again...")
main()
