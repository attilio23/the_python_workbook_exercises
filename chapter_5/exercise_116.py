##
#Determine the perfect numbers between 1 and 10000
from exercise_115 import properDivisors
#Store the upper limit and the lower limit as constants
UPP_LIM=10000
LOW_LIM=1
##Determine if a number is perfect
# @param n the number
# @return True if the number is perfect. False otherwise.
def perfectNumber(n):
    l_p_d=properDivisors(n)
    if sum(l_p_d)==n:
        return True
    return False
#Display the perfect numbers    
def main():
    print("HERE THE PERFECT NUMBERS BETWEEN 1 AND 10000:\n")
    for i in range(LOW_LIM,UPP_LIM+1):
        if perfectNumber(i):
            print(i)
#Call the main function            
main()            