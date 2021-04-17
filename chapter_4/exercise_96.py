##Determine whether a string entered by the user is an integer
##Determine if the string (private of empty spaces) is an integer
# @param string the string to evaluate
# @return True if s represents an integer. False otherwise
def isInteger(string):
    n_s=string.strip()
    i=0
#Check if the first character is "+" or "-" and the length of the string is less than 1    
    if (n_s[i]=="+" or n_s[i]=="-") and len(n_s)>1:
        i=i+1
#Keep looping while i is less than the length of the string        
        while i<len(n_s):
            if n_s[i]<"0" or n_s[i]>"9":
                return False
            i=i+1
        return True    
    else:
#Keep looping while i is less than the length of the string          
        while i<len(n_s):
            if n_s[i]<"0" or n_s[i]>"9":
                return False
            i=i+1
        return True
#Demonstrate the isInteger function               
def main():
    s=input("Enter the string:\n")
    if isInteger(s):
        print("The string represents an integer.")
    else:
        print("The string does not represent an integer.")
#Only call the main function when this file has not been imported        
if __name__=="__main__":
    main()        
