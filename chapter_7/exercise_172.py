##
# Search a file containing a list of words and display all of the words that 
# contain each of the vowels A, E, I, O, U and Y exactly once and in order
# Create a list to store vowels
vowels_list = ["a", "e", "i", "o", "u", "y"]
# Read the name of the file to read from the user
f_n_r = input("Enter the name of the file to read:\n")
try:
# Open the file for reading
    inf = open(f_n_r, "r")
# Create a list to store the words that meet this constraint
    s_v_o_ws = []
# Read the first line from the file
    line = inf.readline()
# Keep looping until we have reached the end of the file
    while line != "":
        line = line.rstrip()
        o_line = line
        line = line.lower()
        l_c = 0
        t = True
        v_c = 0
# Keep looping while l_c is less than the length of line and t is True
        while l_c < len(line) and t:
# Check if the character is a consonant
            if not(line[l_c] in vowels_list):
                l_c = l_c + 1
            else:
# Check if the character matches the current vowel
                if line[l_c] == vowels_list[v_c]:
# Check if the character matches the last vowel
                    if v_c == len(vowels_list) - 1:
                        s_v_o_ws.append(o_line)
                        t = False
                    else:
                        v_c = v_c + 1
                        l_c = l_c + 1    
                else:
                    t = False
# Read the next line from the file
        line = inf.readline()
# Close the file
    inf.close()
# Check if s_v_o_ws is empty   
    if s_v_o_ws:
# Display the result
        print("The words that contain each of the vowels A, E, I, O, U and Y exactly once and in order are:\n")
        for w in s_v_o_ws:
            print(w)
    else:
        print("No word satisfies the constraint")                     
except FileNotFoundError:
# Display an error message if the file to read was not opened successfully
    print("'%s' wasn't found."%f_n_r)    
