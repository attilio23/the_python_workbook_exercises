##
#Display the answers for the first 100 numbers in the Fizz-Buzz game
#Store the limit as constant
limit=100
#Display the answers up to the limit 
for i in range(1,limit+1):
    if i%5==0 and i%3==0:
        print("Fizz Buzz\n")
    elif i%5==0:
        print("Buzz\n")
    elif i%3==0:
        print("Fizz\n")
    else:
        print("%d\n"%i)            