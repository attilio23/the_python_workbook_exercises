##
#Show the name of the frequency of a radiation entered by the user
R_W_u_l=3e9
M_l_l=3e9
M_u_l=3e12
I_L_l_l=3e12
I_L_u_l=4.3e14
V_L_l_l=4.3e14
V_L_u_l=7.5e14
U_L_l_l=7.5e14
U_L_u_l=3e17
X_R_l_l=3e17
X_R_u_l=3e19
#Read the frequency from the user
frequency=float(input("Enter the frequency(in Hertz):\n"))
#Determine the name
if frequency<R_W_u_l:
    name="Radio Waves"
elif M_l_l<=frequency<M_u_l:
    name="Microwaves"
elif I_L_l_l<=frequency<I_L_u_l:
    name="Infrared Light"
elif V_L_l_l<=frequency<V_L_u_l:
    name="Visible Light"
elif U_L_l_l<=frequency<U_L_u_l:
    name="Ultraviolet Light"
elif X_R_l_l<=frequency<X_R_u_l:
    name="X-Rays"
else:
    name="Gamma Rays"
#Display the result
print("The name of the radiation is: %s."%name)    
    
