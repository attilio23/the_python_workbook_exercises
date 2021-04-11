##
#Compute the amount of gas in moles
R=8.314
#Read the value of the pressure, volume and temperature from the user
pressure=float(input("Enter the value of the pressure in Pascal:\n"))
volume=float(input("Enter the value of the volume in liters:\n"))
temperature=float(input("Enter the value of the temperature in degrees Kelvin:\n"))
#Compute the amount of gas in moles
n=(pressure*volume)/(R*temperature)
#Display the result
print("The amount of gas in moles is: %.3f moles "%n)
