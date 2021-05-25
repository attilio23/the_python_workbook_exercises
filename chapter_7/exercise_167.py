##
# Read a file and display all of the words in it that are misspelled
import sys
# Verify that exactly one command line argument (in addition to the .py file) was supplied
if len(sys.argv) != 2:
    print("A file name must be provided as a command line argument.")
    quit()
try:
    inf_1 = open(sys.argv[1], "r")
    w_d = dict()
# Open the file for reading
    inf_2 = open("words.txt", "r")
# Process each line in the file
    for line in inf_2:
        line = line.rstrip()
        w_d[line.capitalize()] = 0    
# Create a list that stores the misspelled words
    m_w_l = []
# Create a list that stores punctuation marks  
    p_m=[",", ".", "?", "!", "-", "'", ":", ";"]
# Create the list of words present in the line
    for line in inf_1:
        line = line.rstrip()
        n_s = ""
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
# Process each word in the list
        for word in w_l_l:
# Check if word is in the keys of w_d
            if not(word.capitalize() in w_d.keys()):
                m_w_l.append(word)
# Close the files
    inf_1.close()
    inf_2.close()
# Check if the list is empty
    if m_w_l != []:
# Display the result
        print("Misspelled words:\n")
        for word in m_w_l:
            print(word)
    else:
        print("There are no misspelled words")                    
except FileNotFoundError:
    print("'%s' wasn't found."%sys.argv[1])
  