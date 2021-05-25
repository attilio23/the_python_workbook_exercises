##
#Detect repeated words in a text file
import sys 
# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("A file name must be provided as a command line argument.")
    quit()
try:
# Open the file for reading
    inf = open(sys.argv[1], "r")
    count = 0
# Create a list that stores punctuation marks  
    p_m=[",", ".", "?", "!", "-", "'", ":", ";"]
    l_e = ""
# Create the list of words present in the line
    for line in inf:
        count = count + 1 
        line = line.rstrip()
        n_s=""
        for i in range(len(line)):
            if i < len(line) - 1:
                if line[i] in p_m and line[i + 1] == " ":
                    pass
                else:
                    n_s = n_s + line[i]
            else:
                if line[i] in p_m:
                    pass
                else:
                    n_s = n_s + line[i]      
        w_l_l = n_s.split()
# Detect repeated words
        if count > 1 and l_e == w_l_l[0]:
            print("Repeated word: '%s'   Lines %d-%d"%(w_l_l[0], count, count - 1))
        for i in range(1, len(w_l_l)):
            if w_l_l[i] == w_l_l[i - 1]:
                print("Repeated word: '%s'   Line %d"%(w_l_l[i], count)) 
        l_e = w_l_l[-1]
# Close the file 
    inf.close()            
except FileNotFoundError:
# Display an error message if the file was not opened successfully    
    print("'%s' wasn't found."%sys.argv[1])        