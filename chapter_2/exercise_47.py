##
#Determine the season from the day of the year entered
#Read the day of the year fom the user
month=input("Enter the month:\n")
day=int(input("Enter the day:\n"))
season=" "
#Determine the season
if (month=="January") and (1<=day<=31):
    season=="Winter"
elif (month=="February") and (1<=day<=28):
    season="Winter"
elif (month=="May") and (1<=day<=31):
    season="Spring"
elif (month=="April") and (1<=day<=30):
    season="Spring"
elif (month=="July") and (1<=day<=31):
    season="Summer"
elif (month=="August") and (1<=day<=31):
    season="Summer"
elif (month=="October") and (1<=day<=31):
    season="Autumn"
elif month=="December":
    if day<21:
        season="Autumn"
    else:
        season="Winter"
elif month=="March":
    if day<20:
        season="Winter"
    else:
        season="Spring"
elif month=="June":
    if day<21:
        season="Spring"
    elif day<=30:
        season="Summer"
elif month=="September":
    if day<22:
        season="Summer"
    elif day<=30:
        season="Autumn"
#Check if the day of the year entered is valid
if season==" ":
    print("The day of the year entered isn't valid")
else:
    print("The day of the year is in the season",season)
