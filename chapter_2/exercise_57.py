##
#Calculate the total cost of a cell phone plan
b_cost=15.00
c_mess_add=0.15
c_minu_add=0.25
c_911=0.44
tax=0.05
#Read the number of minutes and text messages used in this month
minutes=int(input("Enter the number of minutes used:\n"))
messages=int(input("Enter the number of messages used:\n"))
#Compute the total bill amount
t_bill_amount=b_cost+c_911
charge_minu_add=0.0
charge_mess_add=0.0
if minutes>50:
    charge_minu_add=(minutes-50)*c_minu_add
    t_bill_amount=t_bill_amount+charge_minu_add
if messages>50:
    charge_mess_add=(messages-50)*c_mess_add
    t_bill_amount=t_bill_amount+charge_mess_add
t_bill_amount_tax=t_bill_amount*tax    
t_bill_amount=t_bill_amount+t_bill_amount_tax
#Display the result
print("The base charge is $%.2f .\nThe additional minutes charge is $%.2f.\
\nThe additional message charge is $%.2f.\nThe 911 fee is $%.2f .\
\nThe tax is $%.2f .\nThe total bill amount is $%.2f ."%(b_cost,charge_minu_add,
charge_mess_add,c_911,t_bill_amount_tax,t_bill_amount))
    
