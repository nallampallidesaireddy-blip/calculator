class BankAccount :
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.balance = 0
        print(f"\nAccount created successfully for{self.name}!")

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited successfully!")
        else:
            print ("invalid amount.")
        self.display_balance()

    def withdraw(self, amount, enter_pin):
        if enter_pin != self.pin:
            print("incorrect pin!withdraw denied!")
        elif amount<=0:
            print("invalid amount.")
        elif amount > self.balance:
            print("insufficient balance !")
        else:
            self.balance-=amount
            print(f"{amount} withdraw successfully!")
        self.display_balance()


    def display_balance(self):
                print(f"current balance: {self.balance}")
#--- main program---
print("welcome to simple bank system ")
name= input("Enter ur Name:")
pin = input("Enter 4-digits Pin:")

account = BankAccount(name, pin)

while True:
    print("\nselect an option:")
    print("1. Deposit money:")
    print("2. Withdraw money:")
    print("3.Check balance:")
    print("4. Exit:")

    choice = input("Enter your choice(1/2/3/4): ")

    if choice == '1':
        amount =float(input("enter amount to deposit: :"))
        account.deposit(amount)

    elif choice == '2':
        enter_pin = input("Enter ur  pin : ")
        amount=float(input("Enter amount to withdraw: "))
        account.withdraw(amount,enter_pin)
    elif choice == '3':
        enter_pin =input("Enter ur pin : ")
        if enter_pin == account.pin:
            account.display_balance()
        else:
             print("incorrect pin!access denied")
    elif choice =='4':
        print("thank you for using our bank")
        break
    else:
        print("invalid choice!please try again.")






