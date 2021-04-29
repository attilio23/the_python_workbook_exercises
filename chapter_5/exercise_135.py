##
#Display all prime numbers between 2 and the limit
#Store the limit as constant
LIMIT=100
#Create a list to store the numbers
numbers=[]
#Store each number from 0 to the limit in numbers
for i in range(LIMIT+1):
        numbers.append(i)               
numbers[1]=0
p=2
#Keep looping while p is less or equal than the limit
while p<LIMIT+1:   
#Delete any non-prime number by replacing it with zero    
    for i in range(p*2,LIMIT+1,p):
        numbers[i]=0
    p=p+1
#Keep looping while p is less or equal than the limit and equal to zero    
    while p<LIMIT+1 and numbers[p]==0:
        p=p+1
#Display the result        
print("The prime numbers between 2 and %d are:\n"%LIMIT)        
for i in numbers:
    if i!=0:
        print(i)                    