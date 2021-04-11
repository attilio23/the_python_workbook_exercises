##
#Compute the total number of seconds represented by a duration
#Read the number of days, hours, minutes and seconds
days=int(input("Enter the number of days :\n"))
hours=int(input("Enter the number of hours :\n"))
minutes=int(input("Enter the number of minutes :\n"))
seconds=int(input("Enter the number of seconds :\n"))
#Compute the duration in seconds
dur_sec=days*86400+hours*3600+minutes*60+seconds
#Display the result
print("The duration in seconds is:%d seconds"%dur_sec)
