##
#Compute area and volume 
from math import pi
#Read the radius from the user
r=float(input("Enter the radius in meters :\n"))
#Compute area and volume
area=pi*r**2
volume=(4/3)*pi*r**3
#Display the result
print("The area of the circle with radius %.3f meters is: %.3f square meters.\n"\
      "The volume of the sphere with radius %.3f meters is: %.3f cubic meters."%(r,area,r,volume))
