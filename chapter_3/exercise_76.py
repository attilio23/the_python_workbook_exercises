##
#Determine if a phrase is palindrome
#Read the phrase from the user
string=input("Enter the string :\n")
string=string.upper()
string_2=""
i=0
x=1
#Keep looping while i is less than the size of the string
while i<len(string):
#Keep looping while the characters of the string are punctuation marks     
    while (string[i]==" " or string[i]=="!" or \
        string[i]==chr(34) or "'"<=string[i]<="*" or \
            ","<=string[i]<=chr(47) or ":"<=string[i]<="<" or\
                 string[i]==">" or string[i]=="?"):
#If the last character has been reached, exit the intern loop                 
                 if i==len(string)-1:
                     x=0
                     break
                 i=i+1
#If the last character has been reached, exit the inner loop                
    if x==0:
        break                
    string_2=string_2+string[i]
    i=i+1      
j=0
k=len(string_2)-1
is_palindrome=True
#Keep looping while i is less than j
while j<k:
    if string_2[j]!=string_2[k]:
        is_palindrome=False
        break
    j=j+1
    k=k-1
#Display the result    
if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")
