##
#Determine and display the corresponding number of days of the month entered
#Read the name of the month from the user
month=input("Enter the name of the month:\n")
#Determine the corresponding number of days
if month=="November" or month=="September" or month=="April" or month=="June":
    print("30 days")
elif month=="January" or month=="March" or month=="May" or month=="July"\
or month=="August" or month=="October" or month=="December":
    print("31 days")
#Display "28 or 29 days" for February so that leap years are addressed    
elif month=="February":
    print("28 or 29 days")
#Display an error message in case the name entered isn't the name of a month    
else:
    print("The name entered is invalid")
    
    
