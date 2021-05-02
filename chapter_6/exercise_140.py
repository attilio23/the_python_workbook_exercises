##
# View the province or territory associated with the postal code entered by the user, along 
# with whether the address is urban or rural
# Create a dictionary that maps from the first character of the postal code to the
# province or territory name
provinces={"A":"Newfoundland", "B":"Nova Scotia", "C":"Prince Edward Island", \
"E":"New Brunswick", "G":"Quebec", "H":"Quebec", "J":"Quebec", \
"K":"Ontario", "L":"Ontario", "M":"Ontario", "N":"Ontario", "P":"Ontario", \
"R":"Manitoba", "S":"Saskatchewan", "T":"Alberta", "V":"British Columbia", \
"X":"Nunavut or Northwest Territories", "Y":"Yukon"}
# Read the postal code from the user
postal_code=input("Enter the postal code:\n")
#Check if the first and the second characters of the postal code are valid
if (not (postal_code[0] in provinces.keys())) or (postal_code[1]<"0" or postal_code[1]>"9"):
    if not (postal_code[0] in provinces.keys()):
        print("The first character isn't valid.\n")
    if postal_code[1]<"0" or postal_code[1]>"9":
        print("The second character isn't valid.\n")
elif postal_code[1]=="0":
    print("The postal code is for a rural address in",provinces[postal_code[0]])
else:
    print("The postal code is for an urban address in",provinces[postal_code[0]])
