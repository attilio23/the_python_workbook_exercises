##
#Compute the body mass index (BMI)
#Read the value of the height and weight
height=float(input("Enter the value of height in meters:\n"))
weight=float(input("Enter the value of weight in kilograms:\n"))
#Compute the BMI
BMI=weight/(height*height)
#Display the result
print("The body mass index (BMI) is: %.3f "%BMI)
                   
