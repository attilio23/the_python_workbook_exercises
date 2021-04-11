##
#Display the corresponding shape with respect to the number of sides
#Read the number of sides from the user
n=int(input("Enter the number of sides(the range is [3,10]):\n"))
#Determine the corresponding shape and display the result
if n>=3 and n<=10:
    if n==3:
        print("Triangle")
    elif n==4:
        print("Quadrilateral")
    elif n==5:
        print("Pentagon")
    elif n==6:
        print("Hexagon")
    elif n==7:
        print("Heptagon")
    elif n==8:
        print("Octagon")
    elif n==9:
        print("Ennagon")
    else:
        print("Decagon")
else:
    print("The number of sides entered isn't within the specified range")
