##
#Generate a good password, displaying the number of attempts needed
from exercise_100 import randomPassword
from exercise_102 import checkPassword
#Continue generating password until a valid password is generated
def main():
    count=0
    p=randomPassword()
    count=count+1
    while not(checkPassword(p)):
        p=randomPassword()
        count=count+1        
    print("The password is",p)
    print("The number of attempts needed before creating a good password is",count) 
#Call the main function       
main()