##
#Compute the sum of the digits in an integer
F_C=1000
S_C=100
T_C=10
#Read the four-digit integer
n=int(input("Enter the four-digits integer:\n"))
#Compute the sum
s=n//F_C
n_2=n-s*F_C
s=s+(n_2//S_C)
n_3=n_2-(n_2//S_C)*S_C
s=s+(n_3//T_C)
n_4=n_3-(n_3//T_C)*T_C
s=s+n_4
#Display the result
print("The sum is %d ."%s)
