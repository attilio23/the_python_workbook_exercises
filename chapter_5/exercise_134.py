##
#Display all of the sublists of several different lists
##Create a list containing all the sublists of the list
# @param x the list
# @return the list of sublists
def allSublists(x):
    a_sls=[[]]
    i=0
    while i<len(x):
        a_sls.append([x[i]])
        j=i+1
        while j<len(x):
            a_sls.append(a_sls[-1]+[x[j]])
            j=j+1
        i=i+1        
    return a_sls  
#Demonstrate the allSublists function
def main():
    print("The sublists of the list [] are:\n",allSublists([]))
    print("The sublists of the list [1] are:\n",allSublists([1]))
    print("The sublists of the list [1, 2, 3, 4] are:\n",allSublists([1,2,3,4]))
    print("The sublists of the list ['a', 'b', 'c'] are:\n",allSublists(['a','b','c']))
#Call the main function    
main()          