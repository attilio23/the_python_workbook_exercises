##
# Determine if two phrases entered by the user are anagrams
# Create two dictionaries that map from character to frequency
c_p_1={}
c_p_2={}
# Create a list that will contain characters to ignore
p_m=[" ", ".", "?", "!", ".", ",", ":", ";", "-", "[", "]", "(", ")", "{", "}","'","*",chr(35)]
# Read the first phrase from the user
p_1=input("Enter the first phrase:\n").lower()
# Read the second phrase from the user
p_2=input("Enter the second phrase:\n").lower()
# For each loop check whether ch represents a key in c_p_1
for ch in p_1:
    if ch in p_m:
        pass
    elif ch in c_p_1.keys():
        c_p_1[ch]=c_p_1[ch]+1
    else:
        c_p_1[ch]=1    
# For each loop check whether ch represents a key in c_p_2                    
for ch in p_2:
    if ch in p_m:
        pass
    elif ch in c_p_2.keys():
        c_p_2[ch]=c_p_2[ch]+1
    else:
        c_p_2[ch]=1   
# Display the result            
if c_p_1=={} and c_p_2=={}:
    pass
elif c_p_1==c_p_2:
    print("The phrases are anagrams.")
else:
    print("The phrases are not anagrams.")   
