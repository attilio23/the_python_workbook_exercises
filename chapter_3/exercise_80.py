##
#Determine the prime factors of an integer
#Read the integer from the user
n=int(input("Enter the number:"))
#Check if the integer is less than 2
if n<2:
    print("The number entered isn't valid.\n")
else:
#Compute the prime factors     
    print("The prime factors of",n,"is:")
    factor=2
#Keep looping while factor is less than or equal to n     
    while factor<=n:
        if n%factor==0:
#Display the result             
            print("%d"%factor)
            n=n//factor
        else:
            factor=factor+1        
