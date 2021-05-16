##
# Display the first 10 lines of a file whose name is provided as a command line 
# argument
# Store the number of lines as a constant
LINES = 10
import sys
# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("A file name must be provided as a command line argument.")
    quit()
try:
# Open the file for reading    
    inf = open(sys.argv[1], "r")
# Read and display(removing the trailing newline character) the amount of lines specified by LINES
    for i in range(LINES):       
        line = inf.readline()        
        print(line.rstrip())
# Close the file
    inf.close() 
except FileNotFoundError:
# Display an error message if the file was not opened successfully    
    print("'%s' wasn't found."%sys.argv[1])
