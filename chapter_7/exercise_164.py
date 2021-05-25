##
# Determine and display all of the baby names that were used for both boys and girls
# Read the year from the user
year = input("Enter the year:\n")
try:
# Open the file for reading
    inf_b = open("BabyNames/"+year+"_BoysNames.txt")
# Open the file for reading
    inf_g = open("BabyNames/"+year+"_GirlsNames.txt")
# Create three lists to store male names, female names and gender neutral names
    names_b = []
    names_g = []
    g_n_names = []
# Process each line in the file
    for line in inf_b:
        l_line = (line.rstrip()).split()
        names_b.append(l_line[0])
# Process each line in the file
    for line in inf_g:
        l_line = (line.rstrip()).split()
        names_g.append(l_line[0])    
# Close the files
    inf_b.close()
    inf_g.close()
# Check if the number of elements of names_b is less than or equal to the number of elements of names_g
    if len(names_b) <= len(names_g):
# Process each name in names_b
        for name in names_b:
# Check if the name is also present in names_g
            if name in names_g:
                g_n_names.append(name)
    else:
# Process each name in names_g
        for name in names_g:
# Check if the name is also present in names_b
            if name in names_b:
                g_n_names.append(name)
# Check if g_n_names is an empty list
    if g_n_names:
# Display the result
        print("The baby names that were used for both males and females in the year",year,"are:\n")
        for name in g_n_names:
            print(name)
    else:
        print("There were no gender neutral names in the selected year")        
except FileNotFoundError:
# Display an error message if there is no information about the year entered
    print("There is no information for the year entered")