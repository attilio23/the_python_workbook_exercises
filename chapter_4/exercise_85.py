##
#Compute the hypotenuse based on the sides entered from the user
from math import sqrt
##Determine the hypotenuse
#@param side_1 the first side
#@param side_2 the second side
#@return the hypotenuse
def compute_hypo(side_1, side_2):
    hypotenuse=sqrt((side_1**2)+(side_2**2))
    return hypotenuse
#Read the other two sides of the triangle and display the hypotenuse
def main():
    s_1=float(input("Enter the first side of the right triangle :\n"))
    s_2=float(input("Enter the second side of the right triangle :\n"))
#Check if the two sides are valids    
    if s_1>0 and s_2>0:
        hypo=compute_hypo(s_1,s_2)
        print("The hypotenuse is ",hypo)
    else:
        print("The values entered aren't valids.")
#Call the main function        
main()    


    
