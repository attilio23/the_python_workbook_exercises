##
#Determine the greatest common divisor between two numbers entered from the user
#Read the numbers
n=int(input("Enter the first number:\n"))
m=int(input("Enter the second number:\n"))
d=min(n,m)
#Keep looping while d does not evenly divide m or d does not evenly divide n
while m%d!=0 or n%d!=0:
    d=d-1
#Display the result    
print("The greates common divisor between",m,"and",n,"is:",d) 

