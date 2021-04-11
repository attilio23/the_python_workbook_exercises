##
#Compute and display the denominations of the coins that should be used to give that amount of change to the shopper 
PENNY=1
NICKEL=5
DIME=10
QUARTER=25
LOONY=100
TOONY=200
#Read the change from the user
change=int(input("Enter the change:\n"))
#Compute the number of coins
n_toonies=change//TOONY
r=change-n_toonies*TOONY
n_loonies=r//LOONY
r=r-n_loonies*LOONY
n_quarters=r//QUARTER
r=r-n_quarters*QUARTER
n_dimes=r//DIME
r=r-n_dimes*DIME
n_nickels=r//NICKEL
r=r-n_nickels*NICKEL
n_pennies=r//PENNY
#Display the result
print("This is the change:\n")
print("Toonies:%d Loonies:%d Quarters:%d Dimes:%d Nickels:%d Pennies:%d"%(n_toonies,n_loonies,n_quarters,n_dimes,n_nickels,n_pennies))
