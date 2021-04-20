##
#Display a multiplication table that shows the products of all combinations of integers from 1 times 1 up to and including 10 times 10 
print("  ",end='')
#Display the numbers from 1 to 10
for i in range(1,11):
    print("%5d"%i,end='')
print("\n") 
#Compute and display the table of each number from 1 to 10 
for j in range(1,11):
    print("%2d"%j,end='')
    for k in range(1,11):
        print("%5d"%(j*k),end='')
    print("\n")


 
