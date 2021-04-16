##
#Determine the expiry date(gregorian date), based on the purchase date(ordinal date) entered by the user
from exercise_91 import leap
#Store the product can be returned as constant
LAST_DATE=14
##Determine the gregorian date
# @param year the year of the ordinal year
# @param day the day of the ordinal date
# @return the month and the day of the expiry date
def ord_to_gre(year,day):
    d_jan=31
    d_feb=60
    d_mar=91
    d_apr=121
    d_may=152
    d_jun=182
    d_jul=213
    d_aug=244
    d_sep=274
    d_oct=305
    d_nov=335
    d_dic=366
    if not(leap(year)):
        d_feb=d_feb-1 
        d_mar=d_mar-1
        d_apr=d_apr-1
        d_may=d_may-1
        d_jun=d_jun-1
        d_jul=d_jul-1
        d_aug=d_aug-1
        d_sep=d_sep-1
        d_oct=d_oct-1
        d_nov=d_nov-1
        d_dic=d_dic-1
    d=day
    m=1
    if d_jan<d<=d_feb:
        d=d-d_jan
        m=2   
    elif d_feb<d<=d_mar:
        d=d-d_feb
        m=3
    elif d_mar<d<=d_apr:
        d=d-d_mar
        m=4
    elif d_apr<d<=d_may:
        d=d-d_apr
        m=5           
    elif d_may<d<=d_jun:
        d=d-d_may
        m=6
    elif d_jun<d<=d_jul:
        d=d-d_jun
        m=7
    elif d_jul<d<=d_aug:
        d=d-d_jul
        m=8
    elif d_aug<d<=d_sep:
        d=d-d_aug
        m=9
    elif d_sep<d<=d_oct:
        d=d-d_sep
        m=10   
    elif d_oct<d<=d_nov:
        d=d-d_oct
        m=11
    elif d_nov<d<=d_dic:
        d=d-d_nov
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
