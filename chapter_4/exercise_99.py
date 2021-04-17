##
#Determine the next prime number based on the integer entered 
#from the user
from exercise_98 import isPrime
#Determine the next prime number
def nextPrime(n):
    i=n+1
#Keep looping while i isn't a prime number    
    while not(isPrime(i)):
        i=i+1 
    return i  
#Demonstrate the nextPrime function    
def main():
    integer=int(input("Enter the integer:\n"))
    n_p=nextPrime(integer)
    print("The next prime integer is %d"%n_p)
#Call the main function    
main()          