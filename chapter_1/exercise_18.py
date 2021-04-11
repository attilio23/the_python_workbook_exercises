##
#Compute the volume of a cylinder
from math import pi
#Read the radius and the height from the user
radius=float(input("Enter the radius of the cylinder in centimeters:\n"))
height=float(input("Enter the height of the cylinder in centimeters:\n"))
#Compute the volume
volume=radius**2*pi*height
#Display the result
print("The volume of the cylinder is: %.1f cubic centimeters"%volume)
