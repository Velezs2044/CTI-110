#Steven Velez
#3/11/2024
#P3Lab - Branching

#Get info from user
change = int (input("Enter amount of change: "))

#No change back.
if change <= 0:
    print ("No change")

#Calculate how many dollars.
num_dollars = change // 100
change = change - (num_dollars * 100)

#Calculate how many quarters.
num_quarters = change // 25
change = change - (num_quarters * 25)

#Calculate how many dimes.
num_dimes = change // 10
change = change - (num_dimes * 10)

#Calculate how many nickels.
num_nickels = change // 5
change = change - (num_nickels * 5)

#Calculate how many pennies.
num_pennies = change // 1
change = change - (num_pennies * 1)

#Display info to the user.
if num_dollars > 0:
    print (num_dollars, end=" ")
    if num_dollars == 1:
        print ("Dollar")
    else:
        print ("Dollars")

        
if num_quarters > 0:
    print (num_quarters, end=" ")
    if num_quarters == 1:
        print ("Quarters")
    else:
        print ("Quarters")


if num_dimes > 0:
    print (num_dimes, end=" ")
    if num_dimes == 1:
        print ("Dimes")
    else:
        print ("Dimes")


if num_nickels > 0:
    print (num_nickels, end=" ")
    if num_nickels == 1:
        print ("Nickels")
    else:
        print ("Nickels")


if num_pennies > 0:
    print (num_pennies, end=" ")
    if num_pennies == 1:
        print ("Pennies")
    else:
        print ("Pennies")
