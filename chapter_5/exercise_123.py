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
    x=w[0].isupper()
    w=w.lower()
#Check if w starts by vowel or consonant
    if w[0]=="a" or w[0]=="e" or w[0]=="i" or w[0]=="o" or w[0]=="u":
        if w[len(w)-1]=="," or w[len(w)-1]=="." or w[len(w)-1]=="!" or w[len(w)-1]=="?":
            p_m=w[len(w)-1]
            w=w[:len(w)-1]
            w=w+"way"+p_m   
        else:
            w=w+"way"
#Check if x is true            
        if x:
            n_p_w=w[0].upper()+w[1:]
            l_s_p_l.append(n_p_w)
        else:
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
#Check if the last character of w is a punctuation mark            
        if w[len(w)-1]=="," or w[len(w)-1]=="." or w[len(w)-1]=="!" or w[len(w)-1]=="?":
            p_m=w[len(w)-1]
            p_w=w[j:len(w)-1]+p_w+"ay"+p_m
        else:
            p_w=w[j:]+p_w+"ay"
#Check if x is true            
        if x:
            n_p_w=p_w[0].upper()+p_w[1:]
            l_s_p_l.append(n_p_w)  
        else:
            l_s_p_l.append(p_w)
delimeter=" "
print("\n")
#Display the result
print("Your string in Pig Latin:")
s_p_l=delimeter.join(l_s_p_l)
print(s_p_l)