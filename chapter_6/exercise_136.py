##
# Perform a reverse lookup on a dictionary, finding keys that 
# map to a specific value
## Find keys that map to the value
# @param d the dictionary
# @param v the value
# @return the list of keys that map to the value
def reverseLookup(d,v):
# Create a list to store the keys that map to v    
    k_a_v=[]
# Check each key of d    
    for k in d:
# If the current value is equal to v, store the key in k_a_v      
        if d[k]==v:
            k_a_v.append(k)
    return k_a_v
#Demonstrate the reverseLookup function    
def main():
    dctnry={"a": 3, "b": 1, "c": 3, "d": 3, "e": 0, "f": 5}
    print("The keys that map to 3 are:",reverseLookup(dctnry,3))
    print("The keys that map to 7 are:",reverseLookup(dctnry,7))
    print("The keys that map to 0 are:",reverseLookup(dctnry,0))
#Only call the main function when this file has not been imported         
if __name__=="__main__":
    main()              