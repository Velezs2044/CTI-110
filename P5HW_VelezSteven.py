#Steven Velez
#04/21/2024
#P5HW
#Math-quiz

import random

def add_numbers():
  # Set difficulty level (range of numbers)
  lower_bound = 1
  upper_bound = 10

  # Generate random numbers
  number1 = random.randint(lower_bound, upper_bound)
  number2 = random.randint(lower_bound, upper_bound)

  # Keep track of guesses
  guesses = 0

  # Start the quiz loop
  while True:
    # Get user input
    answer = int(input(f"What is {number1} + {number2}? "))
    guesses += 1

    # Check answer
    if answer == (number1 + number2):
      print("Congratulations! You got the answer right.")
      print(f"It took you {guesses} guesses.")
      break
    elif answer < (number1 + number2):
      print("Your guess is too low. Try again.")
    else:
      print("Your guess is too high. Try again.")

def subtract_numbers():
  # Set difficulty level (range of numbers)
  lower_bound = 1
  upper_bound = 10

  # Generate random numbers
  number1 = random.randint(lower_bound, upper_bound)
  number2 = random.randint(lower_bound, upper_bound)

  # Ensure number1 is greater than number2 for subtraction
  if number1 < number2:
    number1, number2 = number2, number1

  # Keep track of guesses
  guesses = 0

  # Start the quiz loop
  while True:
    # Get user input
    answer = int(input(f"What is {number1} - {number2}? "))
    guesses += 1

    # Check answer
    if answer == (number1 - number2):
      print("Congratulations! You got the answer right.")
      print(f"It took you {guesses} guesses.")
      break
    elif answer < (number1 - number2):
      print("Your guess is too low. Try again.")
    else:
      print("Your guess is too high. Try again.")

def main():
  while True:
    # Display menu options
    print("MAIN MENU")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

    # Get user input
    choice = input("Please choose one of the menu options: ")

    # Validate user input
    if choice not in ["1", "2", "3"]:
      print("Invalid input. Please select a number from 1 to 3.")
      continue

    # Exit the program
    if choice == "3":
      print("Exiting program...")
      break

    # Call corresponding function based on user choice
    if choice == "1":
      add_numbers()
    else:
      subtract_numbers()

if __name__ == "__main__":
  main()
