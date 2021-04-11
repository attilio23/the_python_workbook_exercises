##
#Compute the final speed of an object dropped from a precise height
from math import sqrt
G=9.81
V_I=0.00
#Read the value of the height from the user
height=float(input("How high does the height from which the object is dropped measure? Express the value in meters.\n"))
#Compute the final speed
V_F=sqrt(V_I**2+2*G*height)
#Display the result
print("The final speed of the object is:%.2f m/s"%V_F)
