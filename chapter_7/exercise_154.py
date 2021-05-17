##
# Determine and display the frequencies of all letters in a file
import sys
# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("A file name must be provided as a command line argument.") 
    quit()
try:
# Open the file for reading    
    inf = open(sys.argv[1], "r")
# Create a dictionary that maps from letter to frequency    
    l_f = {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, \
"P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0}  
# Read the first line from the file
    line = inf.readline()
# Keep looping until we have reached the end of the file    
    while line != "":
        line = line.rstrip()
# Check every word in the line        
        for ch in line:
            if "A"<=ch<="Z" or "a"<=ch<="z":
                l_f[ch.upper()] = l_f[ch.upper()] + 1
# Read the next line from the file 
        line = inf.readline()
# Close the file        
    inf.close()
# Display the result    
    print("LETTER FREQUENCIES:\n")
    for k in l_f:
        print(k,":",l_f[k])
except FileNotFoundError:
# Display an error message if the file was not opened successfully    
    print("'%s' wasn't found."%sys.argv[1])        