##
#Arithmetic calculations
import math 
#Read the first integer from the user
a=int(input("Enter the first integer\n"))
#Read the second integer from the user
b=int(input("Enter the second integer\n"))
#Compute the sum of a and b
c1=a+b
#Compute the difference when b is subtracted from a
c2=a-b
#Compute the product of a and b
c3=a*b
#Compute the quotient when a is divided by b
c4=a/b
#Compute the remainder when a is divided by b
c5=a%b
#Compute the result of log(a,10)
c6=math.log(a,10)
#Compute the result of a^b
c7=a**b
#Display the results
print("The sum is %d, the difference is %d, the product is %d, "\
      "the quotient is %.3f, the remainder is %d, the result of "\
      "log(a,10) is %.3f, the result of a^b is %d"%(c1,c2,c3,c4,c5,c6,c7))
