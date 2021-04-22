##
#Avoid the user entering duplicate words
#Initialize words to an empty list
words=[]
#Read the first word from the user
word=input("Enter the first word:\n")
#Continue looping until a blank line is entered
while word!="":
#Check if the word entered is in words    
    if not (word in words):
        words.append(word)
#Read the word from the user        
    word=input("Enter the word(blank to quit):\n")
print("\n") 
#Display the result   
for i in words:
    print(i)
