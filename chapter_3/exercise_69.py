##
#Calculate the price of admission for a group visiting a zoo
#Store the prices of admission as constants
Y_2_OR_LESS=0.0
Y_BETW_3_AND_12=14.00
Y_65_OR_OVER=18.00
ALL_OTHER=23.00
#Read the age of the first guest from the user
age=input("Enter the age of the first guest:\n")
t_cost=0.0
#Keep looping while the user enters a non-blank line
while age!="":
    if 0<=int(age)<=2:
        t_cost=t_cost+Y_2_OR_LESS
    elif int(age)<0:
        print("The year entered isn't valid")    
    elif 3<=int(age)<=12:
        t_cost=t_cost+Y_BETW_3_AND_12
    elif int(age)>=65:
        t_cost=t_cost+Y_65_OR_OVER
    else:
        t_cost=t_cost+ALL_OTHER
#Read the age of the next guest from the user         
    age=input("Enter the age of the next guest:\n")
#Display the result     
print("The total cost is $%.2f "%t_cost) 
      