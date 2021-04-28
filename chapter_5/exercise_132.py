##
#Read a mathematical expression in infix form by the user, convert it to 
#postfix form, evaluate it and visualize its value
from exercise_129 import tokenizing
from exercise_130 import unaryOperators
from exercise_131 import infixToPostfix,isInteger
##Calculating the value of a mathematical expression in postfix form
# @param postfix_expression the mathematical expression
# @return the value of the mathematical expression
def evaluatePostfix(postfix_expression):
    values=[]
    for token in postfix_expression:
        if isInteger(token):
            values.append(int(token))
        elif token=="u-":
            n_v=values.pop()
            values.append((-1)*n_v)
        elif token=="+"  or token=="-" or token=="*" or token=="/" or token=="^":
            right=values.pop()
            left=values.pop()
            if token=="+":
                result=left+right
            elif token=="-":
                result=left-right
            elif token=="*":
                result=left*right
            elif token=="/":
                result=left/right
            else:
                result=left**right
            values.append(result)
    return values[0]     
#Demonstrate the evaluatePostfix function                    
def main():
    math_expression=input("Enter a mathematical expression:\n")
    tokens=tokenizing(math_expression)
    unr_ops_tokens=unaryOperators(tokens)
    math_expression_postfix=infixToPostfix(unr_ops_tokens)
    print("The result is:\n",evaluatePostfix(math_expression_postfix))
#Call the main function    
main()
