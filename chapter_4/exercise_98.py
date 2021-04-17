##
#Determine if an integer entered from the user is prime
#Check if the integer is prime
# @param n the integer to check
# @return True if the integer is prime. False otherwise.
def isPrime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True 
#Demonstrate the isPrime function           
def main():
    number=int(input("Enter the number:\n"))
    if isPrime(number):
        print("It's a prime number.")
    else:
        print("It isn't a prime number.")
#Only call the main function when this file has not been imported         
if __name__=="__main__":
    main()                        