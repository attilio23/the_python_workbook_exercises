##
#Compute the weigth amount for a collection of products
W_W=75
W_G=112
#Read the number of widgets from the user
widgets=int(input("What's the number of widgets?\n"))
#Read the number of gizmos from the user
gizmos=int(input("What's the number of gizmos?\n"))
#Compute the weigth amount
weigth=(widgets*W_W)+(gizmos*W_G)
#Display the result
print("The weigth amount is: %.2f grams" %weigth)
