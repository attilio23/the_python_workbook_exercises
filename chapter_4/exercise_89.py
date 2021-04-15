##
#Determine the corresponding ordinal number of the numbers from 1 to 12 
LOW_LIMIT=1
UPP_LIMIT=12
##Determine the ordinal number
#@param n the number 
#@return the ordinal number if n is between 1 and 12. A empty string otherwise.
def determine_ord_number(n):
    if n==1:
        return "first"
    elif n==2:
        return "second"
    elif n==3:
        return "third" 
    elif n==4:
        return "fourth"
    elif n==5:
        return "fifth"
    elif n==6:
        return "sixth"                   
    elif n==7:
        return "seventh"
    elif n==8:
        return "eighth"
    elif n==9:
        return "ninth"
    elif n==10:
        return "tenth"
    elif n==11:
        return "eleventh"
    elif n==12:
        return "twelfth"
    else:
        return "" 
#Demostrate the determine_ord_number function             
def main():
#Display the corresponding ordinal number up to the UPP_LIMIT   
    for i in range(LOW_LIMIT,UPP_LIMIT+1):
        print(determine_ord_number(i))
#Call the main function only if the file has not been imported into another program        
if __name__=="__main__":
    main()                   

