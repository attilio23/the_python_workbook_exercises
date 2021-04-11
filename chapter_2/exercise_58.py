##
#Determine if a year is leap
#Read the year from the user
year=int(input("Enter the year:\n"))
#Determine if it is leap or not and display the result
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("The year %d is leap."%year)
        else:
            print("The year %d isn't leap."%year)
    else:
        print("The year %d is leap."%year)
else:
    print("The year %d isn't leap."%year)


