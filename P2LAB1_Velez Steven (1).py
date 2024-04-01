#Steven Velez
#2/28/2024
#P2LAB1 - Math expessions and f-string

#Get info from user
mpg = float(input("Enter the car's mpg: "))
cost = float(input("Enter the cost for a gallon of gas: "))


#Calculate cost to drive 23, 365, 708 miles
miles_23 = (23/mpg) * cost
miles_365 = (365/mpg) * cost 
miles_708 = (708/mpg) * cost 

#Output info to user
print (f"The cost to drive 23 miles is ${miles_23:.2f} ")
print (f"The cost to drive 365 miles is ${miles_365:.2f} ")
print (f"The cost to drive 708 miles is ${miles_708:.2f} ")
