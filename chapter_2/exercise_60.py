##
#Calculate which day of the week is the first of January based on the year entered from th user
from math import floor
#Read the year from the user
year=int(input("Enter the year:\n"))
#Check if the year is valid
if year>0:
    #Determine the day of the week
    day_of_the_week=(year+floor((year-1)/4)-floor((year-1)/100)+\
    floor((year-1)/400))%7
    if day_of_the_week==0:
        day_in_letters="Sunday"
    elif day_of_the_week==1:
        day_in_letters="Monday"
    elif day_of_the_week==2:
        day_in_letters="Tuesday"
    elif day_of_the_week==3:
        day_in_letters="Wednesday"
    elif day_of_the_week==4:
        day_in_letters="Thursday"
    elif day_of_the_week==5:
        day_in_letters="Friday"
    elif day_of_the_week==6:
        day_in_letters="Saturday"
#Display the result        
    print("The first day of the year %d is \
the day %d of the week,that is, %s."%(year,day_of_the_week,day_in_letters))
else:
    print("The year entered isn't valid.")
