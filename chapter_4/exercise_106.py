##
#Determine the number of days of a month based on the month and the year entered from the user
from exercise_91 import leap
##Determine the number of days of the month of the year
# @param y the year
# @param m the month 
# @return the number of days of the month
def daysMonth(y,m):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        return 31
    elif m==4 or m==6 or m==9 or m==11:
        return 30
    else:
#Check if the year is leap        
        if leap(y):
            return 29
        return 28
#Demonstrate the daysMonth function        
def main():
    year=int(input("Enter the year:\n"))
#Check if the year is valid    
    if year>=1583:
        month=int(input("Enter the month:\n"))
#Check if the month is valid        
        if 1<=month<=12:
            n_days=daysMonth(year,month)
            print("The number of days in the month %d of the year %d is %d ."%(month,year,n_days))
        else:
            print("The month entered isn't valid")
    else:
        print("The year entered isn't valid")
#Only call the main function when this file has not been imported        
if __name__=="__main__":
    main()                                      