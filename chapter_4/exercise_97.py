##
#Display the precedence of the mathematical 
#operator based on the string entered from the user
#Determine the opeator's precedence
# @param o the operator 
# @return 1 if the operator is + or -, 2 if it is * or /,3 if it is ^, -1 otherwise.
def precedence(o):
#Evaluate the operator    
    if o=="+" or o=="-":
        return 1
    elif o=="*" or o=="/":
        return 2
    elif o=="^":
        return 3
    else:
        return -1
#Demonstrate the precedence function        
def main():
    operator=input("Enter the operator:\n")
    if precedence(operator)==-1:
        print("The string entered isn't an operator")
    else:
        print("The operator's precedence is",precedence(operator))
#Only call the main function when this file has not been imported       
if __name__=="__main__":
    main()                                