##
#Display only the words of a string entered from the user
##Create the list of the words
# @param s the string to check
# @return the list of the words of s
def onlyWords(s):
    p_m=[",", ".", "?", "!", "-", "'", ":", ";"]
    n_s=""
    for i in range(len(s)):
        if i<len(s)-1:
            if s[i] in p_m and s[i+1]==" ":
                pass
            else:
                n_s=n_s+s[i]
        else:
            if s[i] in p_m:
                pass
            else:
                n_s=n_s+s[i]      
    return n_s.split()
#Display only the words of a string   
def main():
    phrase=input("Enter the phrase:\n")
    words=onlyWords(phrase)
    print("\n")
    for word in words:
        print(word)
#Only call the main function when this file has not been imported         
if __name__=="__main__":
    main()                 



