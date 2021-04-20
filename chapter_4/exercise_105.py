##
#Convert a number from one numerical base to another
from exercise_104 import hex2int,int2hex
#Store the minimum base and the maximum base as constants
MIN_BASE=2
MAX_BASE=16
##Convert a number from an arbitrary numerical base to base 10
# @param n the number to convert
# @param b the base in which the numer is represented
# @return the equivalent number in base 10
def arb2dec(n,b):
    i=len(n)-1
    j=0
    d_n=0
    if 11<=b<=MAX_BASE:
        while i>=0:
            d_n=d_n+(hex2int(n[i])*(b**j))    
            j=j+1    
            i=i-1
        return d_n 
    while i>=0:
        d_n=d_n+(int(n[i])*(b**j))    
        j=j+1    
        i=i-1
    return d_n 
##Convert a number from base 10 to an arbitrary numerical base
# @param d_n the number to convert
# @param b the base into which the number is to be converted
# @return the equivalent number in base b      
def dec2arb(d_n,b):
    n=""
    q=int(d_n)
    if 11<=b<=MAX_BASE:
        if q>=0:
            r=q%b
            n=int2hex(r)+n
            q=q//b
            while q!=0:
                r=q%b
                n=int2hex(r)+n
                q=q//b
        return n 
    if q>=0:
        r=q%b
        n=str(r)+n
        q=q//b
        while q!=0:
            r=q%b
            n=str(r)+n
            q=q//b
    return n
#Convert a number from an arbitrary base between 2 and 16 to an arbitrary base between 2 and 16
def main():
    number=input("Enter the number to convert:\n")
    o_base=int(input("In what base was the number entered?\n"))
    n_base=int(input("Which base do you want to convert the number to?\n"))
    f=0
    for i in number:
#Check if the number and bases are valid       
        if (MIN_BASE<=o_base<=10 and MIN_BASE<=n_base<=MAX_BASE and "0"<=i<=str(o_base-1)) or \
(11<=o_base<=MAX_BASE and MIN_BASE<=n_base<=MAX_BASE and("0"<=i<="9" or "A"<=i<=chr(ord("F")-(MAX_BASE-o_base)) or \
"a"<=i<=chr(ord("f")-(MAX_BASE-o_base)))):
            pass
        else:
            f=1
            break
#Convert the number        
    if f==0:
        if o_base==10:
            new_number=dec2arb(number,n_base)
        elif n_base==10:
            new_number=str(arb2dec(number,o_base))
        else:
            new_number=arb2dec(number,o_base)
            new_number=dec2arb(str(new_number),n_base)
        print("The number %s in the base %d is equal to %s in the base %d."%(number,o_base,new_number,n_base))        
    else:    
        print("At least one between, the old base, the new base and the number is invalid.") 
#Call the main function             
main()            