##
#Compute the amount in the savings account after 1,2 and 3 years
P_I=0.04
#Read the initial amount of money to deposit from the user 
initial_money=float(input("How much is the amount "\
"of money to deposit at the beginning?\n"))
#Compute the amount after 1,2 and 3 years
amount_1_year=initial_money*P_I+initial_money
amount_2_years=amount_1_year*P_I+amount_1_year
amount_3_years=amount_2_years*P_I+amount_2_years
#Display the result
print("The imports after 1,2 and 3 years are: $%.2f,$%.2f and $%.2f" %(amount_1_year,amount_2_years,amount_3_years))
