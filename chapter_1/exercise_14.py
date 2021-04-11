##
#Compute and display the equivalent number of feet and inches in centimeters
INCHES=12
CENTIMETERS=2.54
#Read the number of feet and inches from the user
n_feet=int(input("Enter the number of feet:\n"))
n_inches=float(input("Enter the number of inches:\n"))
#Display the result 
print("The equivalent number of %d'%.2f'' in centimeters is:%.2f centimeters"%(n_feet,n_inches,n_feet*12*2.54+n_inches*2.54))
