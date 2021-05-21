##
# Produce a password by concatenating two randomly selected words from a file
from random import randrange
try:
# Read the name of the file to read from the user
    f_n_r = input("Enter the name of the file to read:\n")
# Open the file for reading
    inf = open(f_n_r, "r")
# Read the lines from the file
    words = inf.readlines()
# Randomly select the two words
    w_1 = words[randrange(0, len(words) + 1)]
    w_2 = words[randrange(0, len(words) + 1)]
# Keep looping while one of the two words is less than three characters long, 
# the words are less than three characters long, the total length is less than 8, 
# the total length is greater than 10 or the two words are equal
    while len(w_1) < 4 or len(w_2) < 4 or len(w_1 + w_2) < 10 or \
len(w_1 + w_2) > 12 or w_1 == w_2:
# Randomly select the two words
        w_1 = words[randrange(0, len(words) + 1)]
        w_2 = words[randrange(0, len(words) + 1)]
# Display the result
    print((w_1.rstrip()).capitalize() + (w_2.rstrip()).capitalize())
# Close the file
    inf.close()
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully 
    print("'%s' wasn't found."%f_n_r)