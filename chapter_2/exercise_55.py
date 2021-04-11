##
#Determine the color associated with the inserted wavelength
#Read the wavelength from the user
wave_l=float(input("Enter the wavelength(in nanometers):\n"))
#Determine the color
if 380<=wave_l<450:
    color="Violet"
elif 450<=wave_l<495:
    color="Blue"
elif 495<=wave_l<570:
    color="Green"
elif 570<=wave_l<590:
    color="Yellow"    
elif 590<=wave_l<620:
    color="Orange"
elif 620<=wave_l<=750:
    color="Red"
else:
    color=" "
#Check if the inserted wavelength is valid and display the result
if color==" ":
    print("The wavelength entered isn't valid.")
else:
    print("The color associated to the wavelength %.3f nm is:%s."%(wave_l,color))
