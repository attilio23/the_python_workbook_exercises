##
#Determine the type of triangle from the lengths of the sides that are inserted
#Read the lengths of the sides
l_1=float(input("Enter the first length:\n"))
l_2=float(input("Enter the second length:\n"))
l_3=float(input("Enter the third length:\n"))
#Check if the third side inserted is vaild
if abs(l_1-l_2)<l_3<l_1+l_2:
#If the third side is valid determine the type and display the result
    if l_1==l_2:
        if l_1==l_3:
            print("Equilateral")
        else:
            print("Isosceles")
    elif l_1==l_3 or l_2==l_3:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("The third side isn't valid")
        
