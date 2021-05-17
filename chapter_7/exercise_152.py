##
# Create a program that reads lines from a file, adds line numbers, to them, and 
# then stores the numbered lines into a new file
# Read the name of the file to read from the user
f_n_r = input("Enter the name of the file to read:\n")
try:
# Open the file for reading
    inf = open(f_n_r, "r")
    count = 0
# Read the name of the file to read from the user
    f_n_w = input("Enter the name of the file to create:\n")
# Open the file for writing
    outf = open(f_n_w, "w")
# Read the first line from the file
    line = inf.readline()
# Keep looping until we have reached the end of the file
    while line != "":
        count = count + 1
# Write the lines to the file with one number on each line
        outf.write("%d: %s"%(count, line))
# Read the next line from the file
        line = inf.readline()   
# Close the files
    inf.close()
    outf.close()
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully 
    print("'%s' wasn't found."%f_n_r)    

