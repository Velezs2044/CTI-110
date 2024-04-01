#Steven Velez
#3/25/2024
#P3HW2

employee_name = ""
hours_worked = 0
pay_rate = 0
overtime_hours = 0
overtime_pay = 0
regular_pay = 0
gross_pay = 0

#Check to see if the employee has worked overtime.

#Get employee's name.

employee_name = input ("Enter your name: ")

#Get employee's hours worked.

hours_worked = float(input("Enter number of hours worked: "))

#Get employee's pay rate input.

pay_rate = float(input("Enter your pay rate: "))

if hours_worked <= 40:
    overtime_hours = 0
    regular_hours = hours_worked
else:
    overtime_hours = hours_worked - 40
    regular_hours = 40
    
#Calculate the employee's regular pay.

regular_pay = pay_rate * (regular_hours)

#Calculate the employee's overtime pay.

overtime_pay = overtime_hours * pay_rate * 1.5

#Calculate the Employee's gross pay.

gross_pay = regular_pay + overtime_pay


#Display the results.

print("-----------------------------------------------------------------------")

print("Employee's Name: ", employee_name)

print(f"\n {'Hours Worked':<18}    {'Pay Rate':<11}    {'Overtome Hours':<16}    {'Overtime Pay':<13}    {'Regular Pay':<13}    {'Gross Pay':<12} ")

print("------------------------------------------------------------------------------------------------------------------------------------------")

print(f" {hours_worked:<18}     {pay_rate:<11}    {overtime_hours:<16}    {overtime_pay:<13}    ${regular_pay:<13.2f}    ${gross_pay:<12.2f} ")
