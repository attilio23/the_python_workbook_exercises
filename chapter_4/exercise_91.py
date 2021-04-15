##
#Displays the day according to the ordinal 
#date , based on the Gregorian date entered by the user
##Determine if the year is leap
# @param y the year
# @return True if the year is leap. False otherwise.
def leap(y):
    if y%400==0:
        return True
    elif y%100==0:
        return False
    elif y%4==0:
        return True
    else:
        return False
#Determine the day within the year         
def ordinalDate(year,month,day):
    d_w_y=0
    if month>1:
        d_w_y=31
    if month>2:
        is_leap=leap(year)
        if is_leap:
            d_w_y=d_w_y+29
        else:
            d_w_y=d_w_y+28
    if month>3:
        d_w_y=d_w_y+31
    if month>4:
        d_w_y=d_w_y+30
    if month>5:
        d_w_y=d_w_y+31 
    if month>6:
        d_w_y=d_w_y+30
    if month>7:
        d_w_y=d_w_y+31
    if month>8:
        d_w_y=d_w_y+31
    if month>9:
        d_w_y=d_w_y+30
    if month>10:
        d_w_y=d_w_y+31
    if month>11:
        d_w_y=d_w_y+30
    d_w_y=d_w_y+day
    return d_w_y    
#Read the year, the month and the day from the user and display 
#the day within the year for that date    
def main():    
    y=int(input("Enter the year:\n"))
#Check if the year is valid    
    if y>=1583:
        l_y=leap(y)
        m=int(input("Enter the month:\n"))
        d=int(input("Enter the day:\n"))
#Check if the month and the day are valid        
        if ((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)and(1<=d<=31)) or \
((m==4 or m==6 or m==9 or m==11)and(1<=d<=30)) or (l_y==True and m==2 and 1<=d<=29) or \
(l_y==False and m==2 and 1<=d<=28):
            day_within_year=ordinalDate(y,m,d)
            print("The day within the year for the \
date %d/%02d/%02d is %d"%(y,m,\
d,day_within_year))
        else:
            print("The date entered isn't valid.")
    else:
        print("The year entered isn't valid.")
#Call the main function only if the file has not been imported into another program        
if __name__=="__main__":
    main()

                                   
                                        
            

        
