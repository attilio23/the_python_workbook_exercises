##
# Read one or more Python source files and identify functions that are not immediately preceded by a comment
import sys 
# Verify that at least one command line argument (in addition to the .py file) was supplied
if len(sys.argv) < 2:
    print("At least the name of a file name must be provided as a command line argument.")
    quit()
for i in range(1, len(sys.argv)):
    try:
# Open the file for reading
        inf = open(sys.argv[i], "r")
        count = 0        
# Read the first line from the file
        line = inf.readline()
        count = count + 1
        line = line.rstrip()
# Check if line is empty
        if line:
            f_c = line[0]
        else:
            f_c = ""    
# Read the next line
#  from the file
        line = inf.readline()
# Keep looping until we have reached the end of the file
        while line != "":
            count = count + 1
            line = line.rstrip()
# Check if the line is the beginning of a function definition and if the previous line is a comment
            if line[: 4] == "def " and f_c != "#":
                j = 4
                name_file = line[j]
                j = j + 1
# Determine the file name
                while line[j] != "(":
                    name_file = name_file + line[j]
                    j = j + 1
# Display the name of the function that is not preceded by a comment, along with the file name and the line number where the function definition is located
                print("Name function:",name_file,"  Name file:",sys.argv[i],"  Line:",count)        
# Check if line is empty
            if line:
                f_c = line[0]
            else:
                f_c = ""    
# Read the next line from the file
            line = inf.readline()  
# Close the file
        inf.close()
    except FileNotFoundError:
# Display an error message if the file was not opened successfully    
        print("'%s' wasn't found."%sys.argv[i])          
print("END")            