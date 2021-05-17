##
# Display the concatenation of one or more files whose names are provided as 
# command line arguments
import sys
# Verify that at least one command line argument (in addition to the .py file) was supplied
if len(sys.argv) == 1:
    print("At least the name of a file name must be provided as a command line argument.")
    quit()
# Process all of the files provided on the command line
for i in range(1, len(sys.argv)):
    try:
# Open the file for reading  
        inf = open(sys.argv[i], "r")
# Read the first line from the file
        line = inf.readline()
# Keep looping until we have reached the end of the file
        while line != "":
# Display the line(removing the trailing newline character)
            print(line.rstrip())
# Read the next line from the file
            line = inf.readline()
# Close the file
        inf.close()    
    except FileNotFoundError:
# Display an error message if the file was not opened successfully 
        print("'%s' wasn't found."%sys.argv[i])    
               