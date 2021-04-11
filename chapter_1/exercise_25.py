##
#Display the equivalent amount of time in the form D:HH:MM:SS
#Read the value of the duration in seconds from the user
dur_sec=int(input("Enter the value of the duration in seconds :\n"))
#Compute the equivalent amount of time
D=dur_sec//86400
r=dur_sec%86400
HH=r//3600
r=r%3600
MM=r//60
SS=r%60
#Display the result
print("The equivalent amount of time of %d seconds is %02d:%02d:%02d:%02d"%(dur_sec,D,HH,MM,SS))
