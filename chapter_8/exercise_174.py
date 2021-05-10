##
# Compute the gratest common divisor between two positive integers entered from the user
## Calculate the maximum common divisor between the two numbers
# @param a the first number
# @param b the second number
# @return the greatest common divisor, -1 if at least one of the two numbers is negative 
def greatestCommonDivisor(a, b):
# Check if the two numbers are positive integers     
    if a<=0 or b<=0:
        return -1  
# Base case: Since b is null, a is the maximum common divisor              
    if not(b):
        return a
# Recursive case: Set c equal to the remainder when a is divided by b and use
# recursion to compute the greatest common divisor between b and c
    else:
        c=a%b
        return greatestCommonDivisor(b, c)
# Demonstrate the gratestCommonDivisor function
def main():
    f_num=int(input("Enter the first positive integer:"))
    s_num=int(input("Enter the second positive integer:"))
    gcd=greatestCommonDivisor(f_num, s_num)
    if gcd==-1:
        print("The numbers must be positive integers")
    else:
        print("The greatest common divisor of %d and %d is: %d"%(f_num, s_num, greatestCommonDivisor(6, 7)))
# Call the main function
main()        
