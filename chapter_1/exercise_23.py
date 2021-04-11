##
#Compute the area of a regular polygon
#Read the number of sides and the lenght of each side from the user
import math
n=int(input("Enter the number of sides :\n"))
s=float(input("Enter the value of the lenght of each side in meters :\n"))
#Compute the area
area=(n*s**2)/(4*math.tan(math.pi/n))
#Display the result
print("The area of the polygon is :%.2f square meters."%area)
