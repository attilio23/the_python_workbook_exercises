##
#Translating the string entered by the user into Pig Latin language
#Read the string from the user
s_e=input("Enter a string:\n")
w=""
#Create a list to store the words of the string entered
l_s_e=s_e.split()
#Create a list to store the words stored in l_s_e in Pig Latin language
l_s_p_l=[]
#Translate each stored word into l_s_e and store it in l_s_p_l
for i in l_s_e:
    w=i
#Check if w starts by vowel or consonant
    if w[0]=="a" or w[0]=="e" or w[0]=="i" or w[0]=="o" or w[0]=="u":
        w=w+"way"
        l_s_p_l.append(w)       
    else:
        j=0
        p_w=""
        p_w=p_w+w[j]
        j=j+1
#Keep looping while the character of w is different by a vowel        
        while w[j]!="a" and w[j]!="e" and w[j]!="i" and w[j]!="o" and w[j]!="u":
            p_w=p_w+w[j]
            j=j+1
        p_w=w[j:]+p_w+"ay"
        l_s_p_l.append(p_w)
delimeter=" "
print("\n")
#Display the result
print("Your string in Pig Latin:")
s_p_l=delimeter.join(l_s_p_l)
print(s_p_l)
