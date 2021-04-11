##
#Determine the conversion from grade points to letter grades
#Read the grade points from the user
g_p=float(input("Enter the grade points:\n"))
#Compute the corresponding letter grades
if g_p>4.0:
    l_g="A+"
elif 3.85<=g_p<=4.0:
    l_g="A"
elif 3.5<=g_p<3.85:
    l_g="A-"
elif 3.15<=g_p<3.50:
    l_g="B+"    
elif 3.0<=g_p<3.15:
    l_g="B"
elif 2.5<=g_p<2.85:
    l_g="B-"
elif 2.15<=g_p<2.5:
    l_g="C+"
elif 1.85<=g_p<2.15:
    l_g="C"
elif 1.5<=g_p<1.85:
    l_g="C-"
elif 1.15<=g_p<1.5:
    l_g="D+"    
elif 0.5<=g_p<1.15:
    l_g="D"
elif g_p<0.5:
    l_g="F"
#Display the result
print("The grade points",g_p,"is equivalent to",l_g)    
                
