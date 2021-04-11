##
#Convert a distance in feet to inches,yards and miles
IN_PER_FT=12
FT_PER_YD=3
FT_PER_ML=5280
#Read the value of the distance from the user
n_feet=float(input("Enter the value of the distance:\n"))
#Display the result
print("The equivalent of %f feet in inches is:%f,in yards is"\
      ":%f,in miles is:%f"%(n_feet,(n_feet*IN_PER_FT),(n_feet/FT_PER_YD),(n_feet/FT_PER_ML)))             
                   
