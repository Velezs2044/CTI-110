#Steven Velez
#3/6/2014
#P2HW1
#Assignment assess student understanding of lists.

#Ask the user to enter grades for following tests.

Module_1 = float (input("Enter grade for Module 1: "))

Module_2 = float (input("Enter grade for Module 2: "))

Module_3 = float (input("Enter grade for Module 3: "))

Module_4 = float (input("Enter grade for Module 4: "))

Module_5 = float (input("Enter grade for Module 5: "))

Module_6 = float (input("Enter grade for Module 6: "))

#Generate a list according to the inputs.

Grades = []

Grades.append(Module_1)

Grades.append(Module_2)

Grades.append(Module_3)

Grades.append(Module_4)

Grades.append(Module_5)

Grades.append(Module_6)

#print (Grades)

#Display the results

Low_grade = (min(Grades))

High_grade = (max(Grades))

Sum_of_grade =(sum(Grades))

Average_grade = (Sum_of_grade / len(Grades))

print ("\n------------Results----------")

print (f"Lowest Grade:     {Low_grade}")

print (f"Highest Grade:    {High_grade}")

print (f"Sum of Grades:    {Sum_of_grade}")

print (f"Average:          {Average_grade:.2f}")

print ("------------------------------")
