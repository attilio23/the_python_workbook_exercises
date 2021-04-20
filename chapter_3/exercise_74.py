##
#Compute the square root of a number
#Read the number from the user 
x=float(input("Enter the number :\n"))
guess=x/2
#Check if the number is valid
if x>=0:
#Keep looping while the absolute value of the difference between guess*guess and x is greater than 10^-12    
    while abs(guess*guess-x) > 1e-12:
        guess=(guess+x/guess)/2
#Display the result        
    print("The square root of",x,"is:",guess) 
else:
    print("The number entered isn't valid .")       