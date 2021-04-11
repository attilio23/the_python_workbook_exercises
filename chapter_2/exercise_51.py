##
#Determine the real roots of a quadratic function
from math import sqrt
#Read the values of the three constants a,b and c
a=int(input("Enter the value of a:\n"))
b=int(input("Enter the value of b:\n"))
c=int(input("Enter the value of c:\n"))
#Compute the discriminant
d=b**2-4*a*c
#Check if the quadratic function has real roots
if d>=0:
#Compute the real roots and display the result    
    if d==0:
        r=1
        root_1=-b/2*a
        print("The quadratic function %dx^2+%dx+%d has %d real roots, it is: %.3f"%(a,b,c,r,root_1))
    else:
        r=2
        root_1=(-b+sqrt(d))/(2*a)
        root_2=(-b-sqrt(d))/(2*a)
        print("The quadratic function %dx^2+%dx+%d has %d real roots, they are: %.3f and %.3f"%(a,b,c,r,root_1,root_2))
else:
    r=0
    print("The quadratic function %dx^2+%dx+%d has %d real roots"%(a,b,c,r))
