##
#Compute the date of Easter
#Read the year from the user
year=int(input("Enter the year: \n"))
#Compute the date
a=year%19
b=year//100
c=year%100
d=b//4
e=b%4
f=(b+8)//25
g=(b-f+1)//3
h=(19*a+b-d-g+15)%30
i=c//4
k=c%4
l=(32+2*e+2*i-h-k)%7
m=(a+11*h+22*l)//451
month=(h+l-7*m+114)//31
day=((h+l-7*m+114)%31)+1
#Display the date
print("For the year %d , Easter is %02d/%02d "%(year,day,month))
