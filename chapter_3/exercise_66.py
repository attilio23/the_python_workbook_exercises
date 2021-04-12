##
#Round the total cost to the nearest nickel
#Read the initial cost from the user
price=input("Enter the price (in dollars):\n")
t_c=0
cont=0
#Keep looping while the user enters a non-blanck line
while price!="":
    cont=1
    t_c=t_c+float(price)
    price=input("Enter the price (in dollars):\n")
#If no cost is entered, display a error message    
if cont==0 :
    print("No number has been entered.")
else:
#Compute the amount due    
    c_p=(t_c-int(t_c))*100
    r=c_p%5
    if r<2.5:
        c_n=c_p-r
    else:
        c_n=c_p-r+5  
    a_d=int(t_c)+(c_n/100) 
#Display the result         
    print("The total cost is: $%.2f"%t_c)
    print("The amount due is: $%.2f"%a_d)
            