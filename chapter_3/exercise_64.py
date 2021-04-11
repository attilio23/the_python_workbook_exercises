##
#Display the table with the original price, the discount amount and the discounted price
DISCOUNT=0.6
cont=0
price=4.95
#Keep looping until the counter is 5
while cont<5:
    dis_amount=price*DISCOUNT
    dis_price=price-dis_amount
#Display th result    
    print("The original price is:$%5.2f .The discount amount is:$%5.2f .\
The new price is:$%5.2f ."%(price,dis_amount,dis_price))
    price=price+5
    cont=cont+1
    
    
