##
#Conversion from MPG to L/100km
L_P_H_K=235.215
#Read the value of fuel efficiency in MPG
f_e_MPG=float(input("Enter the value of fuel efficiency in American units:\n"))
#Calculation equivalent in L/100km
f_e_L_100_km=L_P_H_K/f_e_MPG
#Display the result
print("The equivalent fuel efficiency in Canadian units is: %.3f L/100km"%f_e_L_100_km)

