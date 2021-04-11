##
#Determine the color of a position on a board chess
#Read a position from the user
position=input("Enter the position:\n")
column=position[0]
row=int(position[1])
remainder=row%2
#Determine the color
if (column=='a' or column=='c' or column=='e' or column=='g') and remainder==0:
    color="white"
elif (column=='b' or column=='d' or column=='f' or column=='h') and remainder==1:
    color="white"
else:
    color="black"
#Display the result
print("The color of the position on the board chess is",color)    
    
