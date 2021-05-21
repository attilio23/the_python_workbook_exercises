##
# Sum all of the numbers entered by the user while ignoring any input that is not
# a valid number
s = 0.0
# Read the first number from the user
number = input("Enter a number:\n")
# Keep looping while the number is different from an empty string
while number:
    try:
# Determine the current sum
        s = s + float(number)
# Display the current sum        
        print("The current sum is:",s)
    except ValueError:
# Display an error message if the input is not numerical
        print("You must enter an integer or a floating point number\n") 
# Read the number from the user
    number = input("Enter a number(blank to quit):\n")    
# Display the sum
print("The sum is:",s)    