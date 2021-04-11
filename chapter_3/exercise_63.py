##
#Compute the average of the numbers entered until the user enters the zero
number=float(input("Enter the number (0 to quit):\n"))
#Use cont to track entered numbers
cont=0
s=0
#Keep looping while the user enters a non-zero number
while number!=0:
    cont=cont+1
    s=s+number
    number=float(input("Enter the number (0 to quit):\n"))   
#If no number has been enterd, enter an appropriate error message    
if cont==0:
    print("No number has been entered!")
else:
    average=s/cont
#Display the result    
    print("The average of the numbers entered is %.2f ."%average)
