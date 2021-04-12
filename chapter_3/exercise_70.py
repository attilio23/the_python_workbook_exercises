##
#Compute the parity bit
#Read the string from the user
string=input("Enter the first string containing 0 and 1:\n")
#Keep looping while the user enter a non-blank line
while string!="":
#Check if the string is eight characters long and contains only 1 and 0    
    if (string.count("0") + string.count("1") == 8) and len(string)==8:
        n_1=string.count("1")
#Compute the parity bit and display the result      
        if n_1%2==0:
            print("The parity bit is 0 .\n")
            string=input("Enter the next string containing 0 and 1:\n")
        else:
            print("The parity bit is 1 .\n")
            string=input("Enter the next string containing 0 and 1:\n") 
    else:
#If an invalid string has been inserted, display a suitable error message        
        print("The string entered isn't valid .\n")
        string=input("Enter the next string containing 0 and 1:\n")           
