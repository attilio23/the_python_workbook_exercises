##
#Randomly generate a ticket for a particular lottery
from random import randrange
#Store the minimum number that can be generated, the maximum number 
#that can be generated and the amount of numbers for the ticket as constants
MX_NUM=49
MN_NUM=1
AM_NUM=6
i=0
#Create a list to store the ticket
ticket=[]
#Keep looping while i is less than AM_NUM
while i<AM_NUM:
    number=randrange(MN_NUM,MX_NUM+1)
#Check if the generated number is already present in the ticket    
    if number in ticket:
        pass
    else:
        ticket.append(number)
        i=i+1   
ticket.sort()
#Display the result
print("Here your ticket:\n")
for i in ticket:
    print(i)        

