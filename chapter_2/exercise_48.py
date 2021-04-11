##
#Determine the astrological sign with respect to the birth date
#Read the birth date from the user
b_month=input("Enter the month of birth:\n")
b_day=int(input("Enter the day of birth:\n"))
#Determine the astrological sign
if (b_month=="December" and b_day>=22) or (b_month=="January" and b_day<=19):
    a_s="Capricorn"
elif (b_month=="January" and b_day>=20) or (b_month=="February" and b_day<=18):
    a_s="Aquarius"
elif (b_month=="February" and b_day>=19) or (b_month=="March" and b_day<=20):
    a_s="Pisces"
elif (b_month=="March" and b_day>=21) or (b_month=="April" and b_day<=19):
    a_s="Aries"
elif (b_month=="April" and b_day>=20) or (b_month=="May" and b_day<=20):
    a_s="Taurus"
elif (b_month=="May" and b_day>=21) or (b_month=="June" and b_day<=20):
    a_s="Gemini"
elif (b_month=="June" and b_day>=21) or (b_month=="July" and b_day<=22):
    a_s="Cancer"
elif (b_month=="July" and b_day>=23) or (b_month=="August" and b_day<=22):
    a_s="Leo"
elif (b_month=="August" and b_day>=23) or (b_month=="September" and b_day<=22):
    a_s="Virgo"
elif (b_month=="September" and b_day>=23) or (b_month=="October" and b_day<=22):
    a_s="Libra"
elif (b_month=="October" and b_day>=23) or (b_month=="November" and b_day<=21):
    a_s="Scorpio"
elif (b_month=="November" and b_day>=22) or (b_month=="December" and b_day<=21):
    a_s="Sagittarius"
print("The astrological sign is:%s"%a_s)    
