#Steven Velez
#2/16/2014
#P1HW2
#For this assignemt you will create a program that does some basic math on numbers that are entered.

#Get user input
budget = float(input("Enter your budget: $"))
destination = input("Enter your travel destination: ")
gas_cost = float(input("Enter amount spent on gas: $"))
accommodation_cost = float(input("Enter amnount spent on accommodation: $"))
food_cost = float(input("Enter amount spent on food: $"))

#Calculate total expenses
total_expenses = gas_cost + accommodation_cost + food_cost

#Calculate remaining budget
remaining_budget = budget - total_expenses

#Display results
print("\n------Travel Expenses-------")
print("Location:", destination)
print("Initial Budget: ", budget)
print("\nFuel: ", gas_cost)
print("Accommodation: ", accommodation_cost)
print("Food: ", food_cost)

print("\nRemaining Budget:", remaining_budget)
