##
# Display the total of all of the values entered by the user 
## Calculate the sum of the numbers entered by the user until
# the user enters a blank line
# @return the total of entered values
def sumNumbers():
# Read the number from the user    
    n=input("Enter a number:\n")
# Base case: The user entered a blank line so the total is 0   
    if n=="":
        return 0.0
    else:
# Recursive case: Convert the inserted line to a number and use 
# recursion to read the next line       
        return float(n)+sumNumbers()
# Demonstrate the sumNumbers function        
def main():
    print("The total is :",sumNumbers())
# Call the main function    
main()                