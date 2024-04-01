#Steven Velez
#3/15/2024
#P3HW1
#This program takes a number grade for six modules, determines average and displays letter grade for average.

mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 4: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

#Add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

#Determine lowest, highest , sum and average for grades
lowest = min(grades)
highest = max(grades)
my_sum = sum(grades)
avg = my_sum / len(grades)

#Determine letter grade for average

#Print lowest, highest, sum and average grades
print("\n-------------Results------------------")
print(f"The lowest grade is:          {lowest:.1f}")
print(f"The highest grade is:         {highest:.1f}")
print(f"The sum of grades is:         {my_sum:.1f}")
print(f"The average grade is:         {avg:.2f}")


print("-------------------------------------")

if avg >= 90:
  print('Your grade is: A')
elif avg >= 80:
  print('Your grade is: B')
elif avg >= 70:
  print('Your grade is: C')
elif avg >= 60:
  print('Your grade is: D')
else:
  print('Your grade is: F')

