##
#Determine whether a licens plate belongs to the old style or the new style
#Read the license plate from the user
licens_plates=input("Enter the license plate(6 or 7 characters):\n")
#Compute the length of the string inserted
length=len(licens_plates)
#Determine the style e display the result
if length==6 and "A"<=licens_plates[0]<="Z" and "A"<=licens_plates[1]<="Z" and\
   "A"<=licens_plates[2]<="Z" and "0"<=licens_plates[3]<="9" and\
   "0"<=licens_plates[4]<="9" and "0"<=licens_plates[5]<="9":
    print("This license plate belongs to the old style.")
elif length==7 and "0"<=licens_plates[0]<="9" and "0"<=licens_plates[1]<="9"\
     and "0"<=licens_plates[2]<="9" and "0"<=licens_plates[3]<="9" and\
     "A"<=licens_plates[4]<="Z" and "A"<=licens_plates[5]<="Z" and\
     "A"<=licens_plates[6]<="Z":
    print("This license plate belongs to the new style.")
#If the inserted plate is not valid, insert an appropriate error message    
else:
    print("The licens plates entered isn't valid")
                
