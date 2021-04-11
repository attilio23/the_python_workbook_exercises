##
#Compute the amount of energy to achieve the desired temperature change
H_C_WATER=4.186
J_TO_KWH=2.777e-7
C_PER_KWH=8.9
#Read the volume of the water and the temperature change from the user
volume=float(input("Enter the amount of water in milliliters:\n"))
temp_change=float(input("Enter the value of the temperature change in degrees Celsius:\n"))
#Compute the amount of energy
energy_J=volume*H_C_WATER*temp_change
#Display the result
print("This is the amount of energy to achieve the desired temperature change: %.3f J\n"%energy_J)
#Compute the conversion from joule to kilowatt hours and the cost of boiling the water 
energy_KWH=energy_J*J_TO_KWH
cost_electricity=C_PER_KWH*energy_KWH
#Display the result
print("The cost of boiling the water is: %.2f cents"%cost_electricity)

