##
# Convert a positive integer entered by the user from decimal form to binary form
## Determine the binary form of a decimal number
# @param d_n the decimal number
# @return the string containing the binary form of the decimal number, an empty
# string if d_n is negative
def decimalToBinary(d_n):
#Check if d_n is negative    
    if d_n<0:
        return ""
# Base cases        
    if d_n==1 :
        return str(d_n)
    if d_n==0 :
        return str(d_n)  
# Recursive case  
    return decimalToBinary(d_n//2)+str(d_n%2)
# Demonstrate the decimalToBinary function        
def main():
    d_number=int(input("Enter a decimal number:\n"))
    b_number=decimalToBinary(d_number)
    if b_number!="":
        print("The decimal number %d in binary form is: %s"%(d_number, b_number))
    else:
        print("The number must be non-negative")    
# Call the main function
main()        

