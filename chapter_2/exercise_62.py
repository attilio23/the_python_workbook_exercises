##
#Simulate a spin of a roulette wheel
from random import randrange
#Randomly determine the wheel space
n=randrange(0,38)
#Display the number that was selected and all of the bets that must be payed
if n==37:
    print("The spin resulted in 00...\nPay 00")
elif n==0:
    print("The spin resulted in 0...\nPay 0")
else:
    if n==1 or n==3 or n==5 or n==7 or n==9 or n==12 or n==14 or n==16 or n==18\
       or n==19 or n==21 or n==23 or n==25 or n==27 or n==30 or n==32 or n==34\
       or n==36:
        c_space="Red"
    else:
        c_space="Black"
    if n%2==0:
        even_odd_space="Even"
    else:
        even_odd_space="Odd"
    if 1<=n<=18:
        series_space="1 to 18"
    else:
        series_space="19 to 36"
    print("The spin resulted in %d...\nPay %d\nPay %s\nPay %s\nPay %s"\
          %(n,n,c_space,even_odd_space,series_space))
    
    
