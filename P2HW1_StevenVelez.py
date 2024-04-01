#Steven Velez
#3/0/2024
#P2HW2
#For this assignemt you will create a program that does some basic math on numbers that are entered. The student's ability to edit and enhance exiting programs.

#Get user input
budget = float(input("Enter your budget: $"))
destination = input("Enter your travel destination: ")
gas_cost = float(input("How much do you think you will spend on gas?: $"))
accommodation_cost = float(input("Apptoximately, how much will you need for accomodation/hotel?: $"))
food_cost = float(input("Last, how much do you need for food?: $"))

#Calculate total expenses
total_expenses = gas_cost + accommodation_cost + food_cost

#Calculate remaining budget
remaining_budget = budget - total_expenses

#Display results
print("\n------Travel Expenses-------")

print(f"Location:\t\t{destination:>9}")

print(f"Initial Budget:\t\t ${ budget:>1,.2f}")

print(f"Fuel:\t\t\t ${gas_cost:>1,.2f}")

print(f"Accommodation:\t\t ${accommodation_cost:>1,.2f}")

print(f"Food:\t\t\t ${food_cost:>1,.2f}")

print("-------------------------------")

print(f"\nRemaining Budget:\t ${remaining_budget:>1,.2f}")
