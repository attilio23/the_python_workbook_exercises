##
#Determine the list of proper divisors of a positive integer entered from the user
##Create the list of proper divisors
# @param n the positive integer
# @return the list of proper divisors
def properDivisors(n):
    p_d=[]
    i=1
#Keep looping while i is less or equal than about half of n    
    while i<=(n//2):   
        if n%i==0:
            p_d.append(i)
        i=i+1
    return p_d    
#Demonstrate the properDivisors function    
def main():
    p_integer=int(input("Enter a positive integer:\n"))
#Keep looping while the user enters a number less or equal than 0 or a number greater than 1   
    while p_integer<=0:
        print("You must enter an integer greater than 0!")
        p_integer=int(input("Enter a positive integer:\n"))
    pro_divisors=properDivisors(p_integer)
    print("Here the proper divisors of %d:\n"%p_integer)
    print(pro_divisors)
#Only call the main function when this file has not been imported        
if __name__=="__main__":
    main()        
