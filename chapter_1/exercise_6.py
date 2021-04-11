##
#Compute the taxe,the tip and the total amount for a meal
TAX=0.10
TIP=0.18
#Read the price of the meal
price=float(input("How much is the meal you ordered?\n"))
#Compute tax
tax_for_meal=price*TAX
#Compute tip
tip_for_meal=price*TIP
#Compute total amount
total_amount=price+tax_for_meal+tip_for_meal
#Display the tax for the meal, the tipo for the meal and the total amount for the meal
print("The tax for the meal is: $%.2f; the tip for the meal is: $%.2f; the "\
      "total amount of the "\
      "meal is: $%.2f" %(tax_for_meal,tip_for_meal,total_amount))
