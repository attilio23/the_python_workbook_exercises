##
#Determine the next day based on the date entered by the user
#Read the year, the month and the day from the user
year=int(input("Enter the year:\n"))
month=int(input("Enter the month:\n"))
day=int(input("Enter the day:\n"))
n_year=year
#Check if the year is leap
if year%400==0:
    is_leap=True
elif year%100==0:
    is_leap=False
elif year%4==0:
    is_leap=True
else:
    is_leap=False
#Determine the next day    
if (1<=month<=12) and (1<=day<=31):
    n_day=0
    if ((month==4 or month==6 or month==9 or month==11) and day==30) or \
       ((month==1 or month==3 or month==5 or month==7 or month==8 or month==10) and day==31) or \
       (month==2 and day==28 and is_leap==False) or (month==2 and day==29 and is_leap==True):
        n_month=month+1
        n_day=1
    elif ((month==4 or month==6 or month==9 or month==11) and (1<=day<30)) or \
         ((month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and (1<=day<31)) or \
         (month==2 and 1<=day<28 and is_leap==False) or (month==2 and 1<=day<29 and is_leap==True):
        n_month=month
        n_day=day+1
    elif month==12 and day==31:
        n_month=1
        n_day=1
        n_year=year+1
#Check if the date entered is valid        
if year<=0 or month<1 or month >=13 or day <1 or day >31 or n_day==0:
        print("The date entered isn't valid")
else:
#Display the result    
        print("The day after %4d-%02d-%02d is %4d-%02d-%02d"%(year,month,day,n_year,n_month,n_day))
