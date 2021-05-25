##
# Redact all occurrences of sensitive words in a text file by replacing them with asterisks
# Read the name of the file to read from the user
o_f_n = input("Enter the name of the original text file:\n")
try:
# Open the file for reading    
    inf_1 = open(o_f_n, "r")
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully
    print("'%s' wasn't found."%o_f_n) 
    quit()
# Read the name of the file to read from the user          
sw_f_n = input("Enter the name of the file that contains the sensitive words:\n")
try:
# Open the file for reading     
    inf_2 = open(sw_f_n, "r")
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully    
    print("'%s' wasn't found."%sw_f_n) 
    quit()
# Read the name of the file to read from the user     
r_f_n = input("Enter the name of the file in which the modified version of the original text will be saved:\n")
try:
# Open the file for reading    
    inf_3 = open(r_f_n, "w")
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully    
    print("'%s' wasn't found."%r_f_n) 
    quit()
# Create a list that stores punctuation marks
p_m=[",", ".", "?", "!", "-", "'", ":", ";"]  
sws = []
# Create the list that will contain sensitive words
for line in inf_2:
    sws.append(line.rstrip())  
# Create the list of words present in the line
for line in inf_1:
    t_line = line
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
# Process each word in w_l_l
    for word in w_l_l:
# Process each sensitive word in sws
        for sw in sws:
            v = (word.lower()).find(sw.lower())
# Check if sw matches word or sw is present in word
            if v != -1:
                v_2 = t_line.find(word)
                t_s = t_line[v_2 + v : v_2 + v + len(sw)]  
# Replace the sensitive word with asterisks
                t_line = t_line.replace(t_s, "*" * len(t_s))
                break
# Write the(potentially modified) line to the file
    inf_3.write(t_line)
# Close the files
inf_1.close()
inf_2.close()
inf_3.close() 
print("END")   