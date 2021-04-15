##
#Determine the expiry date(gregorian date), based on the purchase date(ordinal date) entered by the user
from exercise_91 import leap
#Store the number of days of the months and the period in which the product can be returned as constants
D_JAN=31
D_FEB_L=29
D_FEB_NO_L=28
D_MAR=31
D_APR=30
D_MAY=31
D_JUN=30
D_JUL=31
D_AUG=31
D_SEP=30
D_OCT=31
D_NOV=30
D_DIC=31
LAST_DATE=14
##Determine the gregorian date
# @param year the year of the ordinal year
# @param day the day of the ordinal date
# @return the month and the day of the expiry date
def ord_to_gre(year,day):
    d=day
    m=1
    if leap(year):
        D_FEB=D_FEB_L
    else:
        D_FEB=D_FEB_NO_L       
    if D_JAN<d<=D_JAN+D_FEB:
        d=d-D_JAN
        m=2   
    elif D_JAN+D_FEB<d<=D_JAN+D_FEB+D_MAR:
        d=d-D_FEB-D_JAN
        m=3
    elif D_JAN+D_FEB+D_MAR<d<=D_JAN+D_FEB+D_MAR+D_APR:
        d=d-D_MAR-D_FEB-D_JAN
        m=4
    elif D_JAN+D_FEB+D_MAR+D_APR<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY:
        d=d-D_APR-D_MAR-D_FEB-D_JAN
        m=5           
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN:
        d=d-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=6
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL:
        d=d-D_JUN-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=7
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG:
        d=d-D_JUL-D_JUN-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=8
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP:
        d=d-D_AUG-D_JUL-D_JUN-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=9
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP+D_OCT:
        d=d-D_SEP-D_AUG-D_JUL-D_JUN-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=10   
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP+D_OCT<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP+D_OCT+D_NOV:
        d=d-D_OCT-D_SEP-D_AUG-D_JUL-D_JUN-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=11
    elif D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP+D_OCT+D_NOV<d<=D_JAN+D_FEB+D_MAR+D_APR+D_MAY+D_JUN+D_JUL+D_AUG+D_SEP+D_OCT+D_NOV+D_DIC:
        d=d-D_NOV-D_OCT-D_SEP-D_AUG-D_JUL-D_JUN-D_MAY-D_APR-D_MAR-D_FEB-D_JAN
        m=12      
    if 1<=m<=9:
        m="0"+str(m)
    else:
        m=str(m)
    if 1<=d<=9:
        d="0"+str(d)
    else:
        d=str(d)           
    gre_date=m+"/"+d
    return gre_date
#Read the year and the day of the purchase date and display the expiry date     
def main():
    print("Enter the date you purchased the product(ordinal date):")
    y=int(input("Enter the year:\n"))
#Check if the year is valid    
    if y>=1583:
        d=int(input("Enter the day:\n"))
#Check if the day is valid        
        if (1<=d<=366 and leap(y)==True) or (1<=d<=365 and leap(y)==False):
            expiry_d=LAST_DATE+d
            expiry_y=y
            if expiry_d>366 and leap(y)==True:
                expiry_d=expiry_d-366
                expiry_y=y+1
            elif expiry_d>365 and leap(y)==False:
                expiry_d=expiry_d-365
                expiry_y=y+1
            expiry_date=ord_to_gre(expiry_y,expiry_d)
            print("The expiry date to return the product is %s/%s"%(expiry_y,expiry_date))        
        else:
            print("The date entered isn't valid.")    
    else:
        print("The year entered isn't valid.") 
#Call the main function           
main()                                    
