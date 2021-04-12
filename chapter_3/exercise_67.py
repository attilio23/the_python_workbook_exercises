##
#Compute the perimeter of the polygon based on the points entered
from math import sqrt
#Read the coordinates of the point
x_c_n=input("Enter the first x-coordinate:\n")
y_c_n=input("Enter the first y-coordinate:\n")
x_c_i=float(x_c_n)
y_c_i=float(y_c_n)
x_c_p=x_c_n
y_c_p=y_c_n
p=0.0
#Keep looping while the user enters a non-blanck line
while x_c_n!="":
#Calculate the distance between the next point and the previous point    
    p=p+sqrt((float(x_c_n)-float(x_c_p))**2+(float(y_c_n)-float(y_c_p))**2)
    x_c_p=float(x_c_n)
    y_c_p=float(y_c_n)
    x_c_n=input("Enter the x-coordinate:\n")
    y_c_n=input("Enter the y-coordinate:\n")
#Calculate the distance between the last inserted point and the first inserted point    
p=p+sqrt((float(x_c_p)-x_c_i)**2+(float(y_c_p)-y_c_i)**2)
#Display the result 
print("The perimeter of that polygon is:",p)  