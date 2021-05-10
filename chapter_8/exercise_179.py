##
# Determine the square root of different numbers
## Calculate the square root of the number
# @param n the number for which the square root is being computed
# @return the square root of n
def squareRoot(n, guess = 1.0):
# Base case    
    if abs((guess ** 2) - n) <= 1e-12:
        return guess
# Recursive case
    else:        
        return squareRoot(n, ((guess + (n / guess)) / 2))
# Demonstrate the squareRoot function        
def main():
    print("The square root of 36 is %.3f."%squareRoot(36))
    print("The square root of 2 is %.3f."%squareRoot(2))
    print("The square root of 45.89 is %.3f."%squareRoot(45.89))
    print("The square root of 0.67 is %.3f." % squareRoot(0.67))
# Call the main function
main()                