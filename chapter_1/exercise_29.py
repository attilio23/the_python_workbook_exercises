##
#Compute the wind chill index
#Read the value of the temperature and speed
temperature=float(input("Enter the value of air temperature degrees Celsius:\n"))
speed=float(input("Enter the value of the wind speed in kilometers per hour:\n"))
#Compute the index
WCI=round(13.12+0.6215*temperature-11.37*speed**0.16+0.3965*temperature*speed**0.16)
#Display the result
print("The WCI is: %d"%WCI)
