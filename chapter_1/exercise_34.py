##
#Compute the price od day old bread
PRICE_LOAVE=3.49
SCOUNT=0.60
#Read the amount of loaves of day old bread
loaves=int(input("Enter the number of loaves of day old bread:\n"))
#Compute the price
price=loaves*PRICE_LOAVE
discount=price*0.60
price_with_discount=price-discount
#Display the result
print("The normal price is:   %5.2f dollars"%price)
print("The discount is:       %5.2f dollars"%discount)
print("The total price is:    %5.2f dollars"%price_with_discount)

