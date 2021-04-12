##
#Compute the average of the letter grades entered
A=4.0
A_MINUS=3.7
B_PLUS=3.3
B=3.0
B_MINUS=2.7
C_PLUS=2.3
C=2.0
C_MINUS=1.7
D_PLUS=1.3
D=1.0
F=0
#Read the first letter grade entered
l_g=input("Enter the first letter grade:\n")
s=0.0
cont=0
#Keep looping while the user enters a no-blank line
while l_g!="":
    if l_g=="A":
        g_p=A
    elif l_g=="A-":
        g_p=A_MINUS
    elif l_g=="B+":
        g_p=B_PLUS
    elif l_g=="B":
        g_p=B
    elif l_g=="B-":
        g_p=B_MINUS                
    elif l_g=="C+":
        g_p=C_PLUS
    elif l_g=="C":
        g_p=C
    elif l_g=="C-":
        g_p=C_MINUS
    elif l_g=="D+":
        g_p=D_PLUS
    elif l_g=="D":
        g_p=D 
    else:
        g_p=F
#Compute the sum             
    s=s+g_p
#Count the letter grades entered
    cont=cont+1 
    l_g=input("Enter the letter grade:\n") 
#Display an error message if no letter grades have been entered    
if cont!=0: 
    average=s/cont
    print("The average of the letter grades entered is: %.1f"%average)  
else:
    print("No number has been entered\n")                     