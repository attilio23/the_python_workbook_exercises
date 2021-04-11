##
#Determine the corresponding meaning and amount of an employee's raise based on the rating entered
U_P=0.0
A_P=0.4
M_P=0.6
#Read the rating from the user and initialize the increase
rating=float(input("Enter the rating:\n"))
increase=0.0
#Determine the corresponding meaning and, if there is, the amount of the raise
if rating==0.0:
    meaning="Unacceptable Performance"
elif rating==0.4:
    meaning="Acceptable Performance"
elif rating>=0.6:
    meaning="Meritorious Performance"
else:
    meaning=" "
increase=rating*2400.00    
#Verify whether the inserted rating is valid
if meaning==" ":
    print("The rating entered isn't valid")
else:
    print("The meaning of valuation %.1f is: %s. The amount of the increase is $%.2f"%(rating,meaning,increase))
