##
# Determine if two strings entered by the user are anagrams
# Create two dictionaries that map from character to frequency
c_f_1={}
c_f_2={}
# Read the first string from the user
s_1=input("Enter the first string:\n")
# Read the second string from the user
s_2=input("Enter the second string:\n")
# For each loop check whether ch represents a key in c_f_1
for ch in s_1:
    if ch in c_f_1.keys():
        c_f_1[ch]=c_f_1[ch]+1
    else:
        c_f_1[ch]=1  
# For each loop check whether ch represents a key in c_f_2              
for ch in s_2:
    if ch in c_f_2.keys():
        c_f_2[ch]=c_f_2[ch]+1
    else:
        c_f_2[ch]=1
# Display the result        
if s_1=="" or s_2=="":
    print("At least one of the two strings has not been inserted.")
elif c_f_1==c_f_2:
    print("%s and %s are anagrams."%(s_1,s_2))
else:
    print("%s and %s are not anagrams."%(s_1,s_2))            