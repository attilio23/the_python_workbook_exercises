##
#Display numbers below average, average values (if there are) and 
#values above average, based on the numbers entered by the user
#Create four lists to store the numbers below average, the numbers above average, 
#the average values and the numbers entered from the user 
below_average=[]
above_average=[]
average_values=[]
numbers=[]
#Read the first number from the user
n_s=input("Enter the first number:\n")
#Loop until n_s is a blank line
while n_s!="":
    n=float(n_s)
    numbers.append(n)
    n_s=input("Enter the number(blank to quit):\n")
#Check if numbers is empty    
if numbers==[]:
    print("No numbers have been entered.")
else:
#Compute the average    
    average=sum(numbers)/len(numbers)
#Store the values stored in numbers, in the most suitable list
    for number in numbers:
        if number>average:
            above_average.append(number)
        elif number<average:
            below_average.append(number)
        else:
            average_values.append(number)
#Display the result             
    print("The average of the numbers entered is: %f."%average)
    if below_average!=[]:
        print("The numbers below average are:")
        for number in below_average:
            print(number)
    if average_values!=[]:
        print("The average values are:")
        for number in average_values:
            print(number)
    if above_average!=[]:
        print("The numbers above average are:")
        for number in above_average:
            print(number)                           
