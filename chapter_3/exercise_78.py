##
#Determine the sequence that forms through the Collatz conjecture, based on the number entered by the user
#Read the number from the user
n=int(input("Enter the first number:\n"))
#Keep looping while the user enters a number greater than 0
while n>0:
    print("%d"%n,end='')
    last_term=n
#Keep looping while the last term is not equal to 1    
    while last_term!=1:
#Check if the last term is odd or even and compute the new term of the succession       
        if last_term%2==0:            
            new_n=last_term//2
            last_term=new_n
#Display the result            
            print("%4d"%last_term,end='')
        else:
            new_n=(last_term*3)+1    
            last_term=new_n
#Display the result             
            print("%4d"%last_term,end='')
    print()   
#Read the next number from the user          
    n=int(input("Enter the number:\n"))

