##
# Determine the number of unique characters in a string entered by the user 
# Create a dictionary that maps from character to frequency
u_c={}
# Read the string from the user
s=input("Enter a string:\n")
# For each loop check whether ch represents a key in u_c
for ch in s:
    if ch in u_c.keys():
        u_c[ch]=u_c[ch]+1
    else:
        u_c[ch]=1
# Display the result        
print("The unique characters in the string entered are %d"%len(u_c))        