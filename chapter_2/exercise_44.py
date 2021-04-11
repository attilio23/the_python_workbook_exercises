##
#Determine the name of the individual appearing on the banknote entered by the user
G_W=1
T_J=2
A_L=5
A_H=10
A_J=20
U_S_G=50
B_F=100
#Read the banknote from the user
banknote=int(input("Enter the banknote:\n"))
if banknote==G_W:
    individual="George Washington"
elif banknote==T_J:
    individual="Thomas Jefferson"
elif banknote==A_L:
    individual="Abraham Lincoln"
elif banknote==A_H:
    individual="Alexander Hamilton"
elif banknote==A_J:
    individual="Andrew Jackson"
elif banknote==U_S_G:
    individual="Ulysses S.Grant"
elif banknote==B_F:
    individual="Benjamin Franklin"
else:
    individual=" "
#Display the result
if individual!=" ":
    print("The individual that appears on the $",banknote,"banknote is:",individual)
#If the inserted banknote does not exist, enter an appropriate error message    
else:
    print("The banknote does not exist")
