##
#Display all the magic dates of the 20th century
from exercise_106 import daysMonth
#Store the first year and the last year as constants
FIRST_YEAR=1901
LAST_YEAR=2000
##Determine if the date is a magic date
# @param y the year
# @param m the month
# @param d the day 
# @return True if the date is magic. False otherwise
def magicDates(y,m,d):
    s_y=str(y)
    s_t_c=str(m*d)
    if len(s_t_c)==1:
        s_t_c="0"+s_t_c    
    if s_t_c==s_y[2:]:
        return True
    return False    
#Check every date of the 20th century: if it’s magic, display it              
def main():
    print("THE MAGIC DATES IN THE 20TH CENTURY ARE:\n")
    for i in range(FIRST_YEAR,LAST_YEAR+1):
        for j in range(1,13):
            n_d=daysMonth(i,j)
            for k in range(1,n_d+1):
                if magicDates(i,j,k):
                    print("The date %4d/%02d/%02d is a magic date."%(i,j,k))
#Call the main function    
main()    


