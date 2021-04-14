##
#Find the maximum value of 100 randomly generated integers; also view the number of updates
from random import randrange
#Store the upper limit and the lower limit as constants
UPP_LIM=100
LOW_LIM=1
n=randrange(LOW_LIM,UPP_LIM+1)
print(n)
mx=n
count=0
count_updates=0
#Keep looping while count is less than the upper limit -1
while count<UPP_LIM-1:
    n=randrange(LOW_LIM,UPP_LIM+1)
#Check if the maximum value is less than the number generated  
    if mx<n:
        mx=n
        count_updates=count_updates+1
        print(n,"<== Update")
    else:
        print(n)
    count=count+1
#Display the result    
print("The maximum value found was",mx)    
print("The maximum value was updated",count_updates,"times")
