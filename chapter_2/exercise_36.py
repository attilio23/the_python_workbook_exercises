##
#Compute the conversion from human years to dog years
DY_PER_HY_1=10.5
DY_PER_HY_2=4
#Read the number of human years
h_y=int(input("Enter the number of human years:\n"))
#Conversion
if h_y<0:
    print("You entered a negative number!")
else:
    if h_y<=2:
        print("The equivalent of %d human years is %.1f dog years"%(h_y,(DY_PER_HY_1*h_y)))
    else:
        print("The equivalent of %d human years is %.1f dog years"%(h_y,(DY_PER_HY_1*2+DY_PER_HY_2*(h_y-2))))

