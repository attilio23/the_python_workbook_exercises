##
#Display in reverse order the integers entered from the user, after being stored in a list
#Read the first integer from the user
n=int(input("Enter the first integer:\n"))
#Initialize integers to an empty list
integers=[]
#Keep looping while n is different from zero
while n!=0:
#Add n to integers    
    integers.append(n)
#Read the integer from the user    
    n=int(input("Enter the integer(0 to quit):\n"))
#Check if integers is empty    
if integers==[]:
    print("No integers have been entered.")
else:
#Sort the integers into revers order
    integers.reverse()
#Display the elements of the list
    print("Here are the integers in sorted order:\n")
    for integer in integers:
        print(integer)    