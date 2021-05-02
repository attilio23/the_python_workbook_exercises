##
# Show the paid amount entered by the user using english words   
MN_N=0
MX_N=999
# Convert the paid amount into english words
# @param n the paid amount
# @return the string containing the amount paid in english words
def inEnglishWords(n):
    n=str(n)
# Create three dictionaries that map from the number in digits to the number in english words    
    unit={"1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", \
"8":"eight", "9":"nine"}
    tens={"2":"twenty", "3":"thirty", "4":"forty", "5":"fifty", "6":"sixty", "7":"seventy", \
"8":"eighty", "9":"ninety"}
    nmbrs_10_to_19={"10":"ten", "11":"eleven", "12":"twelve", "13":"thirteen", "14":"fourteen", \
"15":"fifteen", "16":"sixteen", "17":"seventeen", "18":"eighteen", "19":"nineteen"}
    n_ls=""
# Convert n    
    if 10<=int(n)<=19:
        return nmbrs_10_to_19[n]
    elif len(n)==3 and 10<=int(n[1]+n[2])<=19:
         return unit[n[0]]+" hundred and "+nmbrs_10_to_19[n[1]+n[2]]
    else:
        for i in range(-1, -len(n)-1, -1):
            if i==-1 and n[i]!="0":
                n_ls=n_ls+unit[n[i]]
            elif i==-2 and n[i]!="0":
                if n[i+1]!="0":
                    n_ls=tens[n[i]]+"-"+n_ls
                else:
                    n_ls=tens[n[i]]   
            elif i==-3:  
                if n[i+1]!="0" or n[i+2]!="0":
                    n_ls=unit[n[i]]+" hundred and "+n_ls    
                else:
                    n_ls=unit[n[i]]+" hundred"                              
    return n_ls  
# Demonstrate the inEnglishWords function  
def main():    
    intgr=int(input("Enter an amount paid:\n"))
# Check if intgr is valid     
    if intgr<=MN_N or intgr>MX_N:
        print("The amount paid entered isn't valid\n")
    else:
        print("The amount paid %d in letter is %s"%(intgr,inEnglishWords(intgr)))
# Call the main function            
main()
    