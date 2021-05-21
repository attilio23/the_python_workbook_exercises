##
# Examine the words present in a file to determine whether or not they follow
# the "I before E except after C" rule
## Enter the word in the list if it is not present
# @param w the word
# @param ws the list of words
# @return (None)
def inList(w, ws):
    if w[len(w) - 3:] == "...":
        w = w[: len(w) - 3]
    elif  not(w[-1].isalpha()):
        w = w[:len(w) - 1]
    if not(w in ws):
        ws.append(w)
def main():
# Read the name of the file to read from the user
    f_n_r = input("Enter the name of the file to read:\n")
    try:
# Open the file for reading
        inf = open(f_n_r, "r")
        r_y = []
        r_n = []
        w_l = []
# Read the first line from the file
        line = inf.readline()
# Keep looping until we have reached the end of the file
        while line != "":
            w_l = (line.rstrip()).split()
# Check every word of the line
            for word in w_l:
                t_s = word.lower()
                if t_s.find("cei") != -1:
                    inList(t_s, r_y)
                elif t_s.find("cie") != -1:
                    inList(t_s, r_n)
                elif t_s.find("ie") != -1:
                    inList(t_s, r_y)
                elif t_s.find("ei") != -1:
                    inList(t_s, r_n)        
# Read the next line from the file
            line = inf.readline()
# Close the file
        inf.close()
# Display the result
        print("The words that follow the rule in the file are: %d\nThe words that violate the rule in the file are: %d"%(len(r_y),len(r_n)))        
    except FileNotFoundError:
# Display an error message if the file to read was not opened successfully
        print("'%s' wasn't found."%f_n_r)        
# Call the main function
main()