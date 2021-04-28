##
#Transforming a mathematical expression entered from
#the user from infix form to postfix form
from exercise_129 import tokenizing
from exercise_130 import unaryOperators
##Determine if the string (private of empty spaces) is an integer
# @param string the string to evaluate
# @return True if s represents an integer. False otherwise
def isInteger(string):
    n_s=string.strip()
    i=0
    if (n_s[i]=="+" or n_s[i]=="-") and len(n_s)>1:
        i=i+1        
        while i<len(n_s):
            if n_s[i]<"0" or n_s[i]>"9":
                return False
            i=i+1
        return True    
    else:         
        while i<len(n_s):
            if n_s[i]<"0" or n_s[i]>"9":
                return False
            i=i+1
        return True
##Determine the opeator's precedence
# @param o the operator 
# @return 1 if the operator is + or -, 2 if it is * or /,3 if it is ^, -1 otherwise.        
def precedence(o):    
    if o=="+" or o=="-":
        return 1
    elif o=="*" or o=="/":
        return 2
    elif o=="u-" or o=="u+":
        return 3    
    elif o=="^":
        return 4
    else:
        return -1     
##Transforming the mathematical expression
# @param infix_expression the mathematical expression 
# @return the list of tokens representing the equivalent postfix expression       
def infixToPostfix(infix_expression):
    operators=[]
    postfix=[]
    for token in infix_expression:
        if isInteger(token):
            postfix.append(token)
        if token=="+" or token=="-" or token=="/" or token=="^" or token=="*" or token=="u-" or token=="u+":
            while operators!=[] and operators[-1]!="(" and precedence(token)<precedence(operators[-1]):
                postfix.append(operators.pop())
            operators.append(token)
        if token=="(":
            operators.append(token)
        if token==")":
            while operators[-1]!="(":
                postfix.append(operators.pop())
            operators.remove("(")
    while operators!=[]:
        postfix.append(operators.pop())           
    return postfix
#Demonstrate the infixToPostfix function    
def main():
    math_expression=input("Enter a mathematical expression:\n")
    tokens=tokenizing(math_expression)
    unr_ops_tokens=unaryOperators(tokens)
    print("The list containing the mathematical expression in postfix form:\n")
    print(infixToPostfix(unr_ops_tokens))
if __name__=="__main__":
    main()
