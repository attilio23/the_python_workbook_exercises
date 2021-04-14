##
#Find the number coin flips needed to achieve three consecutive equal outcomes
from random import randrange
#Store the general limit,the upper limit and the lower limit as constants
LIMIT_G=10
UPP_LIM=2
LOW_LIM=1
s=0
#Display the flips up to the general limit
for i in range(LIMIT_G):
    count=0
    count_h=0
    count_t=0
#Keep looping while count_h is less than 3 and count_t is less than    
    while count_h<3 and count_t<3:
        flip=randrange(LOW_LIM,UPP_LIM+1)
        if flip==1:
            count_t=0
#Display the outcome             
            print("H",end='')
            count_h=count_h+1
        else:
            count_h=0
#Display the outcome             
            print("T",end='')
            count_t=count_t+1
        count=count+1
#Display the number of flips        
    print("(%d flips)"%count)
    s=s+count   
average=s/LIMIT_G
#Disaplay the average 
print("On average, %.1f flips were needed."%average)                

        

    
