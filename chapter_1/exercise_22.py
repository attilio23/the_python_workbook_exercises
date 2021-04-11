##
#Compute the area of a triangle
#Read the lenght of the three sides
from math import sqrt
s1=float(input("Enter the lenght of the first side in meters :\n"))
s2=float(input("Enter the lenght of the second side in meters :\n"))
s3=float(input("Enter the lenght of the third side in meters :\n"))
if s3<s1+s2 and s3>abs(s1-s2):
    #Compute the area
    s=(s1+s2+s3)/2
    area=sqrt(s*(s-s1)*(s-s2)*(s-s3))
    #Display the result
    print("The area of the triangle is: %.2f square meters"%area)
else:
    print("The third side is invalid!")
