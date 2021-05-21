##
# Remove all of the comments from a Python source file
try:
# Read the name of the file to read from the user
    f_n_r = input("Enter the name of the file for reading:\n")
# Read the name of the file to write from the user
    f_n_w = input("Enter the name of the file for writing:\n")
# Open the file for reading
    inf = open(f_n_r, "r")
# Open the file for writing
    outf = open(f_n_w, "w")
# Read the first line from the file to read
    line = inf.readline()
# Keep looping until we have reached the end of the file
    while line != "":
        line = line.rstrip()
        i = 0
        f = 0
# Keep looping while i is less than the length of the line
        while i < len(line):
# Check if the character is equal to "#"
            if line[i] == "#":
                f = 1
# Write the line without comment to the file
                outf.write(line[: i] + "\n")
                break
            i = i + 1
# Check if f is null
        if not(f):
# Write the line to the file
            outf.write(line + "\n")
# Read the next line from the file
        line = inf.readline()
# Close the files
    inf.close()
    outf.close()    
    print("END")     
except FileNotFoundError:
    print("A problem occurred while accessing the files.")

