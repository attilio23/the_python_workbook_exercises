##
# Determine whether it is possible to form the dollar amount entered by 
# the user with a precise number of coins, always entered by the user
from itertools import combinations_with_replacement
## Determine whether or not it is possible to construct a particular total using a 
# specific number of coins
# @param d_a the dollar amount
# @param n_c the number of coins
# @return True if d_a can be formed with n_c coins 
def possibleChange(d_a, n_c, i = 0):
    c_l = [0.25, 0.10, 0.05, 0.01]
    p_c_l = list(combinations_with_replacement(c_l, n_c))
# Base case    
    if i < len(p_c_l) and d_a == round(sum(p_c_l[i]), 4):
        return True
# Recursive case        
    if i < len(p_c_l):
        i = i + 1
        return possibleChange(d_a, n_c, i)
# Demonstrate the possibleChange function        
def main():
    dollar_amount = float(input("Enter the dollar amount:\n"))
    number_coins = int(input("Enter the number of coins:\n"))
    if possibleChange(dollar_amount, number_coins):
        print("The entered dollar amount can be formed using the number of coins indicated.")
    else:
        print("The entered dollar amount can't be formed using the number of coins indicated.")    
# Call the main function
main()
