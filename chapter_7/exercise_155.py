##
# Display the word(or words) that occur most frequently in a file
# Read the name of the file to read from the user
f_n = input("Enter the name of the file:\n")
try:
# Open the file for reading
    inf = open(f_n, "r")
# Read the first line from the file
    line = inf.readline()
    p_m = [",", ".", "?", "!", "-", "'", ":", ";"]
    w_l = []
    w_f ={}
# Keep looping until we have reached the end of the file
    while line != "":
        line = line.rstrip()
        n_s = ""
# Identify the words present in each line
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
        n_s = n_s.lower()            
        w_l = w_l + n_s.split()
# Read the next line from the file
        line = inf.readline()
# Update the frequency of each word present in the file
    for word in w_l:
        if not(word in w_f.keys()):
            w_f[word] = 1
        else:
            w_f[word] = w_f[word] + 1
# Display the result
    print("The most frequently recurring words in the file are:\n")        
    for k in w_f:
        if w_f[k] == max(list(w_f.values())):
            print("%s\n"%k)        
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully
    print("'%s' wasn't found."%f_n)
