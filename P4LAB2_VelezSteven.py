#Steven Velez
#03/27/2024
#P4LAB2
#LAB: Output Range with Increment of 5. Use a while loop.

#Get two integer values from user.

var1 = int(input("Enter the smaller integer: "))

var2 = int(input("Enter the larger integer: "))

#While var1 is larger, allow the user to re-enter the values.

while var1 >= var2:
    print("First number must be smaller. Try again: ")
    
    var1 = int(input("Enter the smaller integer: "))
    
    var2 = int(input("Enter the larger integer: "))

#The while loop has broken. The values have been entered correctly.

for num in range(var1, var2+1, 5):
    print(num, end = " ")
