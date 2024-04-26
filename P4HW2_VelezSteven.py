#Steven Velez
#04/01/2024
#P4HW2
# Create a program that calculates the gross pay for multiple employees.

total_employees = 0

total_overtime = 0

total_regular = 0

total_gross = 0

while True:
    employee_name = input("Enter the employee's name or \"Done\" to terminate: ")
    if employee_name.upper() == "DONE":
        break

    hours_worked = float(input("How many hours did {} work? ".format(employee_name)))
    pay_rate = float(input("What is {}'s pay rate? ".format(employee_name)))

    overtime = 0
    if hours_worked > 40:
        overtime = hours_worked - 40
    regular_pay = hours_worked * pay_rate
    overtime_pay = overtime * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay

    print("\nEmployee name: ", employee_name)
    
    print(f"\n{'Hours Worked':<17}{'Pay Rate':<17}{'Overtime':<17}{'Regular Pay':<17}{'Overtime Pay':<17}{'Gross Pay':<17} ")
    print("---------------------------------------------------------------------------------------------------")
    print(f"{hours_worked - overtime:<17}${pay_rate:<17}{overtime:<17}${regular_pay:<17}${overtime_pay:<17}${gross_pay:<17}")
    print

    #print("\nRegular Hours: ", hours_worked - overtime)

    #print("Overtime:", overtime)

    #print("Regular Pay: ${:.2f}".format(regular_pay))

    #print("Overtime Pay: ${:.2f}".format(overtime_pay))

    #print("Gross Pay: ${:.2f}".format(gross_pay))

    total_employees += 1

    total_overtime += overtime_pay

    total_regular += regular_pay

    total_gross += gross_pay

print("\nTotal number of employees entered: ", total_employees)

print("Total amount paid for overtime: ${:.2f}".format(total_overtime))

print("Total amount paid for regular hours: ${:.2f}".format(total_regular))

print("Total amount paid in gross: ${:.2f}".format(total_gross))
