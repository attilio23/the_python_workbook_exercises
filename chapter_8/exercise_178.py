##
# Determine if a word entered by the user is a palindrome
# Check if a word is a palindrome  
# @param w the word
# @return True if w is a palindrome. False otherwise
def isPalindrome(w):
    w=w.lower()
# Base cases    
    if w=="":
        return True
    if len(w)==1:
        return True         
    if w[0]!=w[-1]:
        return False
# Recursive case        
    else:
        return isPalindrome(w[1:len(w)-1])    
# Demostrate the isPalindrome function    
def main():
    word=input("Enter a word:\n")
    if isPalindrome(word):
        print("It's a palindrome")
    else:
        print("It isn't a palindrome") 
# Call the main function           
main()                    