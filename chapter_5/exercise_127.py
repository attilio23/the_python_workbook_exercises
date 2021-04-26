##
#Determine if a list of values is in sorted order (either ascending or descending)
##Check if a list of values is already sorted
# @param l_n the list to check
# @return True if the list is ordered. False otherwise
def isInSortedOrder(l_n):
    n_l_n=sorted(l_n)
    if n_l_n==l_n:
        return True
    else:
        n_l_n.reverse()
        if n_l_n==l_n:
            return True
    return False
#Demonstrate the isSorted function    
def main():
    numbers=[]
    number=input("Enter the number:\n")
    while(number!=""):
        numbers.append(int(number))
        number=input("Enter the number (blank to quit):\n")
    if isInSortedOrder(numbers):
        print("The list is already sorted")
    else:
        print("The list is not yet sorted") 
#Call the main function               
main()            
