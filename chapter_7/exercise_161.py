##
# Read a file containing information about chemical elements and stores it in one or more appropriate data structures; display the informations
# of the chemical elements based on the input from the user
# Open the file for reading
inf = open("elements.txt", "r")
delimeter = ","
# Create a list to store information of chemical elements
l_c_es = []
for line in inf:
    l_c_es.append((line.rstrip()).split(delimeter))
# Read the information about the chemical element from the user
c_e = input("Enter the name, symbol or number of protons of a chemical element:\n")
# Keep looping while the user enter a non-blank line
while c_e:
    try: 
# Check if all characters in the string are digits
        if c_e.isdigit():
# Display the result
            print("Name: %s     Symbol:%s"%(l_c_es[int(c_e) - 1][2], l_c_es[int(c_e) - 1][1]))
# Check if all characters in the string are in the alphabet
        elif c_e.isalpha():
# Check the number of protons of each element with the number of protons inserted
            for l_c_e in l_c_es:
                if c_e == l_c_e[1] or c_e == l_c_e[2]:
                    p_n = int(l_c_e[0])
                    break
# Display the result
            print("Number of protons:\t%d"%p_n)
# Totally remove the definition for p_n
            del p_n
        else:
            print("Invalid input")    
    except:
# Indicate that the input provided is invalid if no element exists for the name, 
# symbol or number of protons entered
        print("Invalid input")        
# Read the information about the chemical element from the user
    c_e = input("Enter the name, symbol or number of protons of a chemical element(blank to quit):\n")  
# Close the file
inf.close()      
print("END")                

