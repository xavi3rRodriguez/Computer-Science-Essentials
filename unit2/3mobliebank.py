#1st National Bank of Browntown Online Banking Application


class Customer():
    #This is an OBJECT. It has properties of Withdraw, Deposit, BalanceCheck
    def __init__ (self, name, balance = 100.00):
        self.name = name
        self.balance = balance
        print("Account made for", name, " Current Balance: $", balance)

    def withdraw(self,amount):
        self.balance = self.balance - amount
        return self.balance
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    
    def BalanceCheck(self,balance):
        return self.balance


print("Welcome to the 1st National Bank of Browntown App")
print("All new customers get $100 deposited into their account for signing up!")
print()
name = input("Let's Get Started! What is your name: ")
customer = Customer(name)
loop = 1
#options
while loop == 1:
    print("What would you like to do: | (1) Withdraw | (2) Deposit | (3) Check Balance | (4) Quit |")
    choice = input("->")


    #Withdraw
    if choice == "1":
        print("How much are you withdrawing")
        amount = float(input("->"))
        customer.withdraw(amount)
        print("You have withdrawn ", amount)

    #depositing
    if choice == "2":
        print("how much are you depositing")
        amount = float(input("->"))
        customer.deposit(amount)
        print("you have deposited", amount)

    #current balance
    if choice == "3":
        print("your curent balance",amount)
    
    #quiting 
    elif choice == "4":
        print("you have ended the program")
        break

else:
    print("ERROR try again")