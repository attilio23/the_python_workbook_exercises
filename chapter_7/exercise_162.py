##
# Read a list of words from a file and determine what proportion of the words use each letter of the alphabet
l_f = {"A" : 0, "B" : 0, "C" : 0, "D" : 0, "E" : 0, "F" : 0, "G" : 0, "H" : 0, "I" : 0, "J" : 0, "K" : 0, "L" : 0, "M" : 0, "N" : 0, "O" : 0, \
"P" : 0, "Q" : 0, "R" : 0, "S" : 0, "T" : 0, "U" : 0, "V" : 0, "W" : 0, "X" : 0, "Y" : 0, "Z" : 0}
f_n_r = "words.txt"
try:
# Open the file for reading
    inf = open(f_n_r, "r")
# Read the first line from the file
    line = inf.readline()
    count = 0
# Keep looping until we have reached the end of the file
    while line != "":
        l_line = (line.rstrip()).split()
        count = count + len(l_line)
# Check every word of the line 
        for w in l_line:
            l_characters = []
# Check every character of the word of the line
            for ch in w:
                if ("A" <= ch.upper() <= "Z") and (not(ch.upper() in l_characters)):
                    l_characters.append(ch.upper())
# Update the values of l_f
            for ch in l_characters:
                l_f[ch] = l_f[ch] + 1
# Read the next line from the file
        line = inf.readline()
# Close the file
    inf.close()
# Display the result
    for k in l_f:
        print("%s occupies %.2f percent of the words"%(k, (l_f[k])*100/count))
# Determine the minimum value
    s_p = min(l_f.values())     
# Display the result
    for k in l_f:
        if l_f[k] == s_p:
            print("The letter %s occupies the smallest part of the words"%k)
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully
    print("'%s' wasn't found."%f_n_r)