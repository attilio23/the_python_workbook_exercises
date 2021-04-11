##
#Conversion from degrees Celsius to degrees Fahrenheit and degrees Kelvin
#Read the temperature in degrees Celsius from the user
temperature_C=float(input("Enter the value of the temperature in degrees Celsius:\n"))
#Compute the equivalent temperature in degrees Fahrenheit and degrees Kelvin
temperature_F=temperature_C*1.8+32
temperature_K=temperature_C+273.15
#Display the result
print("%.2f degrees Celsius are equivalent to %.2f degrees Fahrenheit and %.2f degrees Kelvin ."%(temperature_C,temperature_F,temperature_K))


