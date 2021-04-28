##
#Identify unary + and - operators in a list of tokens and replace them with u+ and
#u- respectively
from exercise_129 import tokenizing
##Replace unary + and - operators respectively with u+ and u-
# @param ts the list of tokens
# @return the list of tokens where the unary + and - operators have been substituted
def unaryOperators(ts):
    n_ts=[]
    if ts[0]=="-" or ts[0]=="+":
        n_ts.append("u"+ts[0])
    else:
        n_ts.append(ts[0])     
    for i in range(1,len(ts)):
        if (ts[i]=="-" or ts[i]=="+") and (ts[i-1]=="/" or ts[i-1]=="-" \
or ts[i-1]=="^" or ts[i-1]=="+" or ts[i-1]=="*" or ts[i-1]=="(" or \
ts[i-1]=="[" or ts[i-1]=="{"):
             n_ts.append("u"+ts[i])
        else:
            n_ts.append(ts[i])     
    return n_ts
#Demonstrate the unaryOperators function    
def main():
    math_expression=input("Enter a mathematical expression:\n")
    tokens=tokenizing(math_expression)
    print("Tokens:\n",tokens)
    unr_ops_tokens=unaryOperators(tokens)
    print("Tokens (marking the unary operators):\n",unr_ops_tokens)
#Call the main function    
if __name__=="__main__":
    main()             
