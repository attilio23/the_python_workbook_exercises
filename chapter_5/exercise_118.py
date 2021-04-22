##
#Determine if a sentence entered from the user is a palindrome
from exercise_117 import onlyWords
#Read the sentence from the user
sentence=input("Enter a sentence:\n")
sentence=sentence.lower()
l_s=onlyWords(sentence)
#Check if the string entered is a palindrome and display the result
if len(l_s)==0:
    print("No words were entered.")
elif len(l_s)==1:
    print("One word was entered.")
elif len(l_s)%2==0:
    l_p2=l_s[len(l_s)//2:]
    l_p2.reverse()
    if l_s[:len(l_s)//2]==l_p2:
        print("It's a palindrome") 
    else:
        print("It isn't a palindrome")    
elif len(l_s)%2==1:
    l_p2=l_s[(len(l_s)//2):]
    l_p2.reverse()
    if l_s[:(len(l_s)//2)+1]==l_p2:
        print("It's a palindrome")
    else:
        print("It isn't a palindrome")    
