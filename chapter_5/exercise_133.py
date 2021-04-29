##
#Determine if a list is a sublist of another list; the empty list is a sublist of any
#list, a list is a sublist of itself
##Verify that the hypothetical sub-list is a sub-list of the list
# @param larger the list
# @param smaller the hypothetical sublist
# @return True if smaller is a sublist of larger. False otherwise
def isSublist(larger,smaller):
    if len(larger)<len(smaller) or (len(smaller)==len(larger) and smaller!=larger):
        return False 
    elif smaller==[]:
        return True
    elif smaller==larger:
        return True
    else:
        for i in range(len(larger)):
            if larger[i]==smaller[0] and (i+(len(smaller)-1)<=(len(larger))-1):
                if smaller==larger[i:i+len(smaller)]:
                    return True  
    return False
#Demonstrate the isSublist function    
def main():
    l=[]
    s=[]
    s_i=input("Add the first item to Smaller:\n")
    while s_i!="":
        s.append(s_i)
        s_i=input("Add an item to Smaller:\n")
    l_i=input("Add the first item to Larger:\n")
    while l_i!="":
        l.append(l_i)
        l_i=input("Add an item to Larger:\n")
    if isSublist(l,s):
        print("Smaller is a sublist of Larger")
    else:
        print("Smaller isn't a sublist of Larger")
#Call the main function        
main()                     
