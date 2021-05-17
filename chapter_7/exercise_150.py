##
# Display the last 10 lines of a file whose name is provided as a command line argument
import sys
# Store the number of last lines to display as constant
LAST_LINES = 10
# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("A file name must be provided as a command line argument.") 
    quit() 
try:
# Create a list to store the last 10 lines
    lines = []
# Open the file for reading    
    inf = open(sys.argv[1], "r")
    count = 0
# Read the first line from the file
    line = inf.readline()
    count = count + 1
# Keep looping until we have reached the end of the file 
    while line != "":
        if count <= LAST_LINES:
            lines.append(line)
        else:
            lines.pop(0)
            lines.append(line)    
        count = count + 1
# Read the next line from the file
        line = inf.readline()
# Close the file        
    inf.close()    
    if len(lines) < 10:
        print("The file contains less than 10 lines:")  
# Display the result          
    for line in lines:
        print(line.rstrip())    
except FileNotFoundError:
# Display an error message if the file was not opened successfully    
    print("'%s' wasn't found."%sys.argv[1])        
   