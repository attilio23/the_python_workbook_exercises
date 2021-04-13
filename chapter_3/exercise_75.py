##
#Determine if a string is a palindrome
#Read the string from the user
string=input("Enter the string:\n")
i=0
j=len(string)-1
is_palindrome=True
#Keep looping while i is less than j
while i<j:
    if string[i]!=string[j]:
        is_palindrome=False
        break
    i=i+1
    j=j-1
#Display the result    
if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")
