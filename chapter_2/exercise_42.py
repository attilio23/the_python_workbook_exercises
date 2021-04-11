##
#Determine the corresponding frequency with respect to the name of the inserted note
C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=392.00
A4=440.00
B4=493.88
#Read the name of the note from the user
note=input("Enter the name of the note:\n")
f_l=note[0]
s_l=int(note[1])
#Verify that the name entered by the user is valid
if (f_l=='A' or f_l=='B' or f_l=='C' or f_l=='D' or f_l=='E' or f_l=='F' or f_l=='G') and 0<=s_l<=8:
#Determine the corresponding frequency
    if f_l=='A':
        frequency=A4/2**(4-s_l)
    elif f_l=='B':
        frequency=B4/2**(4-s_l) 
    elif f_l=='C':
        frequency=C4/2**(4-s_l)  
    elif f_l=='D':
        frequency=D4/2**(4-s_l)  
    elif f_l=='E':
        frequency=E4/2**(4-s_l)
    elif f_l=='F':
        frequency=F4/2**(4-s_l)
    else :
        frequency=G4/2**(4-s_l)
    print("The frequency is: %.2f"%frequency)   
else:
    print("The name entered isn't valid")
