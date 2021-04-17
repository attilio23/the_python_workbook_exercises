##
#Generate a random password
from random import randrange
#Store the maximum length, the minimum length, the maximum position in the ASCII table and the minimum position in the ASCII table as constants
MAX_L=10
MIN_L=7
MAX_P=126
MIN_P=33
#Determine the password
# @return the random password
def randomPassword():
    l=randrange(MIN_L,MAX_L+1)
#Initialize empty the random password    
    password=""
    i=0
#Keep looping while i is less than the lenght of the password
    while i<l:
        password=password+chr(randrange(MIN_P,MAX_P+1))
        i=i+1
    return password
#Demonstrate the randomPassword function    
def main():
    print("Here the random password:%s"%randomPassword())
#Only call the main function when this file has not been imported    
if __name__=="__main__":
    main()            

