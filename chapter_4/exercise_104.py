##Convert hexadecimal digit to decimal digit
# @param s the hexadecimal digit to convert
# @return the corresponding decimal digit, -1 otherwise
def hex2int(s):
    if "0"<=s<="9":
        return int(s)
    elif "A"<=s<="F" or "a"<=s<="f":
        s=s.upper()
        if s=="A":
            return 10
        elif s=="B":
            return 11
        elif s=="C":
            return 12
        elif s=="D":
            return 13
        elif s=="E":
            return 14
        else:
            return 15  
    else:
#Display an appropriate error message if the value is outside the range        
        print("The value is outside the range.\n")
        return -1
##Convert decimal digit to hexadecimal digit
# @param n the decimal digit to convert
# @return the corresponding hexadecimal digit, -1 otherwise        
def int2hex(n):
    if 0<=n<=9:
        return str(n)
    elif 10<=n<=15:
        if n==10:
            return "A"
        elif n==11:
            return "B"
        elif n==12:
            return "C"
        elif n==13:
            return "D"
        elif n==14:
            return "E"
        else:
            return "F"  
    else:
#Display an appropriate error message if the value is outside the range        
        print("The value is outside the range.\n") 
        return -1                                                                    