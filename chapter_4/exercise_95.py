##
#Capitalize a string entered from the user 
##Capitalize the string
# @param string the string to capitalize
# @return the string for which the capitalization has been realized
def capitalize_it(string):
    c_string=string
    i=0
    while i<len(string) and c_string[i]==" ":
        i=i+1
    if i<len(string):    
        c_string=c_string[0:i]+c_string[i].upper()+string[i+1:len(c_string)]
    i=0
    while i<len(string):
        if c_string[i]=="." or c_string[i]=="?" or c_string[i]=="!":
            i=i+1
            while i<len(string) and c_string[i]==" ":
                i=i+1
            if i<len(string):
                c_string=c_string[0:i]+c_string[i].upper()+c_string[i+1:len(c_string)]
                
        i=i+1    
    i=1    
    while i<len(string)-1 :
        if c_string[i]=="i" and c_string[i-1]==" " and (c_string[i-1]==" " or c_string[i+1]=="." or \
            c_string[i]=="?" or c_string[i]=="!" or c_string[i]=="'"):
            c_string=c_string[0:i]+c_string[i].upper()+c_string[i+1:len(c_string)]
        i=i+1      
    return c_string
#Read the string from the user and demonstrate the capitalize_it function    
def main():
    s=input("Enter the string:\n")
    c_s=capitalize_it(s)
    print("Here the correct string:\n%s"%c_s)
#Call the main function    
main()    


