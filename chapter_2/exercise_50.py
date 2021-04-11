##
#Determine the  magnitude descriptor from the magnitude value entered
#Read the magnitude value
magnitude=float(input("Enter the magnitude value:\n"))
#Determine the corresponding descriptor
if magnitude<2.0:
    descriptor="Micro"
elif 2.0<=magnitude<3.0:
    descriptor="Very Minor"
elif 3.0<=magnitude<4.0:
    descriptor="Minor"    
elif 4.0<=magnitude<5.0:
    descriptor="Light"
elif 5.0<=magnitude<6.0:
    descriptor="Moderate"
elif 6.0<=magnitude<7.0:
    descriptor="Strong"
elif 7.0<=magnitude<8.0:
    descriptor="Major"
elif 8.0<=magnitude<10.0:
    descriptor="Great"
else:
    descriptor="Meteoric"
#Display the result     
print("An earthquake of magnitude %.1f is considered a %s earthquake"%(magnitude,descriptor))    
