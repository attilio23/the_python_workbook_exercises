##
# Convert a roman number entered from the user to an integer
## Determine the corresponding integer
# @param r_n the roman number
# @return the corresponding integer
def romanToInteger(r_n):
    r_i={"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
# Base case
    if r_n=="":
        return 0
# Recursive cases        
    if len(r_n)>=2 and r_i[r_n[0]]<r_i[r_n[1]]:     
        return -r_i[r_n[0]]+romanToInteger(r_n[1:len(r_n)])
    else:
        return r_i[r_n[0]]+romanToInteger(r_n[1:len(r_n)])
# Demonstrate the romanToInteger function
def main():
    roman_number=input("Enter a roman number:\n")
    print("The corresponding integer is:",romanToInteger(roman_number))
# Call the main function
main()                