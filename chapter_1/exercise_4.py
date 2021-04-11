#width field required
width=float(input("Enter the width of the field in feet:\n"))
#length field required
length=float(input("Enter the length of the field in feet:\n"))
#area calculation
area_in_square_feet=width*length
area_in_acres=area_in_square_feet/43560
#print area value
print("The area of the field measures %.3f acres" %area_in_acres)
