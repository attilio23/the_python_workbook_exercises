##
#Determine the corresponding decimal number
#Read the binary number from the user
binary_number=input("Enter the binary number :\n")
i=len(binary_number)-1
j=0
x=0
decimal_number=0
#Keep looping while i is greater or equal to 0
while i>=0:
#Check if the character is 1     
    if binary_number[i]=="1":
        decimal_number=decimal_number+(2**j)
    elif binary_number[i]!="0":
        x=1
        break     
    j=j+1    
    i=i-1
#Display the result 
if x!=0:
    print("The binary number entered isn't valid.\n")
else:
    print("The corresponding decimal number is %d."%decimal_number)        
