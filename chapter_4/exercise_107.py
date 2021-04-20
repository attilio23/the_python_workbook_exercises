##
#Reduce a fraction entered by the user to lowest terms
#Determine the fraction reduced to lowest terms
# @param n the numerator
# @param d the denominator
# @return the numerator and the denominator of fraction reduced to lowest terms 
def fractionLowestTerms(n,d):
    if n==0:
        return (0,1)
    gcd=min(n,d)
#Keep looping while gcd does not evenly divide d or gcd does not evenly divide n
    while d%gcd!=0 or n%gcd!=0:
        gcd=gcd-1
    new_n=n//gcd
    new_d=d//gcd
    return(new_n,new_d)
#Demonstrate the fractionLowestTerms function    
def main():
    numerator=int(input("Enter the numerator(integer and positive):\n"))
#Check if the numerator is valid    
    if numerator>=0:
        denominator=int(input("Enter the denominator(integer,positive and different from zero):\n"))
#Check if the denominator is valid        
        if denominator>0:
            (new_numerator,new_denominator)=fractionLowestTerms(numerator,denominator)
            print("The fraction %d/%d reduced to lowest terms is: %d/%d"%(numerator,denominator,new_numerator,new_denominator))
        else:
            print("The denominator entered isn't valid.")
    else:
        print("The numerator entered isn't valid.")   
#Call the main function                 
main()            