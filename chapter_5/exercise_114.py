##
#Display the negative integers first, then the zeros finally the positive 
#integers, according to the order of insertion of the user
#Initialize zeros,p_integers and n_integers to an empty list
zeros=[]
p_integers=[]
n_integers=[]
integers=[]
#Read the first integer from the user
s_integer=input("Enter the first integer:\n")
#Continue looping until a blank line is entered
while s_integer!="":
    integer=int(s_integer)
#Check if the integer entered is positive,negative or zero    
    if integer>0:
        p_integers.append(integer)
    elif integer<0:
        n_integers.append(integer) 
    else:
        zeros.append(integer)
#Read the integer from the user        
    s_integer=input("Enter the integer(blank to quit):\n")
#Create the list by storing all the integers entered by the user
integers=n_integers+zeros+p_integers
#Display the result
for integer in integers:
    print("%4d"%integer,end="")