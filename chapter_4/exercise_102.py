##
#Check if a password entered from the user is valid
#Store the minimum length of the password as constant
MIN_LEN=8
##Determine if the password is valid
# @param p the password to check
# @return True if the password is valid. False otherwise.
def checkPassword(p):    
    n_l_l=0
    n_u_l=0
    n_d=0
#Check if each character of the password is a lowercase letter, an 
#uppercase letter or a digit     
    for i in p:
        if "a"<=i<="z":
            n_l_l=n_l_l+1
        elif "A"<=i<="Z":
            n_u_l=n_u_l+1
        elif "0"<=i<="9":
            n_d=n_d+1
    if len(p)>=MIN_LEN and n_u_l!=0 and n_l_l!=0 and n_d!=0:
        return True
    return False
#Demonstrate the checkPassword function    
def main():
    password=input("Enter the password:\n")
    if checkPassword(password):
        print("The password is valid.")
    else:
        print("The password isn't valid")    
#Only call the main function when this file has not been imported    
if __name__=="__main__":
    main()                     