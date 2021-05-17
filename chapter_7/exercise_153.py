##
# Identify the longest word(s) in a file
# Read the name of the file to read from the user
f_n_r = input("Enter the name of the file to read:\n")
try:
# Open the file for reading
    inf = open(f_n_r, "r")
    longest_word = ""
    longest_words = []
# Read the first line from the file
    l = inf.readline()
# Keep looping until we have reached the end of the file
    while l != "":
        word = ""
        line = l.rstrip()
# Check every word in the line
        for i in range(len(line) + 1):
            if i == len(line) or line[i] == " ":
                if len(word) == len(longest_word):
                    longest_words.append(word)
                elif len(word) > len(longest_word):
                    longest_word = word
                    longest_words = [word]
                word = ""       
            else: 
                word = word + line[i]             
# Read the next line from the file
        l = inf.readline() 
# Close the file        
    inf.close()       
# Display the result
    print("The size of the longest word(s) is:",len(longest_word),"\nThe longest word(s):")        
    for mx_w in longest_words:
        print(mx_w)   
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully 
    print("'%s' wasn't found."%f_n_r)    
