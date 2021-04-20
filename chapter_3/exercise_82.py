##
#Determine the corresponding binary number
#Read the decimal number from the user
decimal_number=input("Enter the decimal number :\n")
result=""
q=int(decimal_number)
#Check if q is greater or equal than 0
if q>=0:
    r=q%2
    result=str(r)+result
    q=q//2
#Keep looping while q is not equal to 0    
    while q!=0:
        r=q%2
        result=str(r)+result
        q=q//2
#Display the result        
    print("The corresponding binary number is %s."%result)  
else:
    print("The decimal number entered isn't valid.\n")   

