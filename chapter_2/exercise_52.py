##
#Determine the conversion from letter grades to grade points
#Read the letter grade from the user
l_g=input("Enter the letter grade:\n")
#Check if the letter grade entered is valid and compute the corresponding grade points
if (l_g=="A+") or (l_g=="A"):
    g_p=4.0
elif l_g=="A-":
    g_p=3.7
elif l_g=="B+":
    g_p=3.3
elif l_g=="B":
    g_p=3.0
elif l_g=="B-":
    g_p=2.7
elif l_g=="C+":
    g_p=2.3
elif l_g=="C":
    g_p=2.0
elif l_g=="C-":
    g_p=1.7
elif l_g=="D+":
    g_p=1.3
elif l_g=="D":
    g_p=1.0
elif l_g=="F":
    g_p=0    
else:
    g_p=" "
#Display the result
if g_p==" ":
    print("The letter grade entered isn't valid")
else:
    print("The letter grade",l_g,"is equivalent to",g_p)
