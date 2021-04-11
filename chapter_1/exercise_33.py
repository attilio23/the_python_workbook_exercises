#Sort 3 integers
#Read 3 integers from the user
i1=int(input("Enter the first integer:\n"))
i2=int(input("Enter the second integer:\n"))
i3=int(input("Enter the third integer:\n"))
#Sort
x=min(i1,i2,i3)
y=max(i1,i2,i3)
z=(i1+i2+i3)-(x+y)
#Display the result
print("Here are the numbers from the smallest to the largest: %d,%d,%d"%(x,z,y))
