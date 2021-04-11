##
#Determine the name of the fixed-date holiday according to the day of the year
#Read the day of the year from the user
month=int(input("Enter the month:\n"))
day=int(input("Enter the day:\n"))
#Check that the day and month are valid
if (1<=day<=31) and (1<=month<=12):
#Determine the corresponding holiday e dislay the result    
    if day==1 and month==1:
        n_h="New Year's Day"
    elif day==1 and month==7:
        n_h="Canada day"
    elif day==25 and month==12:
        n_h="Christmas Day"
    else:
        n_h=" "
    if n_h==" ":
        print("The inserted day and month do not correspond to any fixed-date holiday")
    else:
        print(n_h)
else:
    print("The day or month isn't valid or the day and the month aren't valid")
