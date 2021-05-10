##
# Calculate the edit distance between two strings entered by the user
## Determine the edit distance between the two strings
# @param s the first string
# @param t the second string
# @return the edit distance between s and t
def stringEditDistance(s, t):
    if len(s) == 0:
        return len(t)
    elif len(t) == 0:
        return len(s)
    else:
        cost = 0
        if s[-1] != t[-1]:
            cost = 1
        d1 =  stringEditDistance(s[: len(s) - 1], t) + 1
        d2 =  stringEditDistance(s, t[: len(t) - 1]) + 1   
        d3 =  stringEditDistance(s[: len(s) - 1], t[: len(t) - 1]) + cost 
        return min(d1, d2, d3)     
# Demonstrate the stringEditDistance function
def main():
    s_1=input("Enter the first string:\n")
    s_2=input("Enter the second string:\n")
    print("The edit distance between the strings", s_1,"and", s_2,"is", stringEditDistance(s_1, s_2))
# Call the main function
main()            