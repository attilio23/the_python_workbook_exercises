##
#Determine the corresponding noise in relation to the inserted decibel level
J=130
G_L=106
A_C=70
Q_R=40
#Read the decibel level from the user
d_l=int(input("Enter the decibel level (the range is[40,130]):\n"))
#Determine the corresponding noise
noise=" "
if  40<=d_l<=130:
#If the decibel level is among the listed noises, display a message indicating the noises between which the value is included
    if d_l==Q_R:
        noise="Quiet Room"
    elif Q_R<d_l<A_C:
        noise="The decibel value is between Quiet Room and Alarm Clock"
    elif d_l==A_C:
        noise="Alarm Clock"
    elif A_C<d_l<G_L:
        noise="The decibel value is between Alarm Clock and Gas Lawnmower"
    elif d_l==G_L:
        noise="Gas Lawnmower"
    elif G_L<d_l<J:
        noise="The decibel value is between Gas Lawnmower and Jackhammer"
    else:
        noise="Jackhammer"
#Display the result and if the decibel level isn't in the specified range, display a suitable error message
if noise==" ":
    print("The decibel level entered is outside the specified range!")
else:
    print(noise)
