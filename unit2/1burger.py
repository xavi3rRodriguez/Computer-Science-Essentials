#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06
totalTax = 0.06
#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please? ->  ")
print()
print("Thanks " + name)
print()
print()

#-----------------------------------------------------------------------------------------------
#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: (1)Burgers, (2)Sides, (3)Drinks, (4)Complete Order.")
    menu = input("-> ")
#--------------------------------------------------------------------------------------------
    if menu == "1":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: mega burger $19.99")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "HAMBURGER":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "CHEESEBURGER":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "WESTERN BURGER":
            totalCost = totalCost+ 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        #BURGER 4: Mega burger
        elif burgerChoice == "Mega burger":
            totalCost = totalCost+ 19.99
            print("You added Mega burger to your order")
            print("Your total cost so far: $", totalCost)
            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELCTION
        else:
            print("please make a valid choice")
#----------------------------------------------------------------------------------------------
    elif menu == "2":
        #IF THEY WANT TO ADD A SIDE :
        print("We offer the following sides:")
        print("1: cheese $500")
        print("2: french fries $3.00")
        print("3: mozzarella sticks $3.99")
        print()
        sideChoice = input("What would you like (input a number 1-3): ")
        #side 1: cheese
        if sideChoice == "cheese":
            totalCost = totalCost + 500
            print("You added cheese to your order")
            print("Your total cost so far: $", totalCost)

        #side 2: french fries
        elif sideChoice == "french fries":
            totalCost = totalCost + 3.00
            print("You added french fries to your order")
            print("Your total cost so far: $", totalCost)

        #side 3: mozzarella sticks
        elif sideChoice == "mozzarella sticks":
            totalCost = totalCost+ 3.99
            print("You added mozzarella sticks to your order")
            print("Your total cost so far: $", totalCost)
         #error
        else:
            print("please make a valid choice")
#-------------------------------------------------------------------
    elif menu == "3":
        print("drinks")
        #IF THEY WANT TO ADD A drink :
        print("We offer the following Drinks:")
        print("1: mountain dew 3.00")
        print("2: big Gulp $8.00")
        print("3: liquid green $90.99")
        print()
        drinkChoice = input("What would you like (input a number 1-3): ")
        #side 1: mountain dew
        if drinkChoice == "mountain dew":
            totalCost = totalCost + 3.00
            print("You added mountain dew to your order")
            print("Your total cost so far: $", totalCost)

        #side 2: big Gulp
        elif drinkChoice == "big Gulp":
            totalCost = totalCost + 8.00
            print("You added big Gulp to your order")
            print("Your total cost so far: $", totalCost)

        #side 3: liquid green
        elif drinkChoice == "liquid green":
            totalCost = totalCost+ 90.99
            print("You added liquid green to your order")
            print("Your total cost so far: $", totalCost)
        #error
        else:
            print("please make a valid choice")
#---------------------------------------------------------------------
    elif menu == "4":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        print("order finished")
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * totalTax
        total = float(totalCost + totalTax)
        print("Total Tax: $", tax)
        print("Grand Total: $ ", total)
        #Finish this section to give you a grand total as well as print your complete order
 
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you", name , "for eating with us!")