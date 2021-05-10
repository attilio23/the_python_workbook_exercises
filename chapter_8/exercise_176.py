##
# Display the phonetic spelling of a word entered from the user
## Determine the phonetic spelling of a word
# @param s the word
# @return the phonetic spelling of the word
def phoneticSpelling(s):
    s=s.upper()
    l_w={"A":"Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta", "E":"Echo", \
"F":"Foxtrot", "G":"Golf", "H":"Hotel", "I":"India", "J":"Juliet", "K":"Kilo", \
"L":"Lima", "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa", "Q":"Quebec", \
"R":"Romeo", "S":"Sierra", "T":"Tango", "U":"Uniform", "V":"Victor", "W":"Whiskey", \
"X":"Xray", "Y":"Yankee", "Z":"Zulu"}
# Base case
    if s=="":
        return ""
# Recursive cases        
    if not (s[0] in l_w.keys()):
        return phoneticSpelling(s[1:len(s)])    
    else:
        return l_w[s[0]]+" "+phoneticSpelling(s[1:len(s)])
# Demonstrate the phoneticSpelling function
def main():
    word=input("Enter a word:\n")
    if phoneticSpelling(word):
        print(phoneticSpelling(word))    
# Call the main function
main()            
