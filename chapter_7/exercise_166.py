##
# Read the baby names data set keeping track of each 
# distinct name used for a boy and each distinct name 
# used for a girl
## Store the first year and the last year as constants
FIRST_YEAR = 1900
LAST_YEAR = 2012
# Create two lists to store male names and female names 
b_names = []
g_names = []
# Process each year in the range
for year in range(FIRST_YEAR, LAST_YEAR + 1):
# Open the file for reading
    inf_b = open("BabyNames/"+ str(year) +"_BoysNames.txt")
# Open the file for reading
    inf_g = open("BabyNames/"+ str(year) +"_GirlsNames.txt")
# Process each line in the file
    for line in inf_b:
        l_line = (line.rstrip()).split()
# Check if the name is already present
        if not(l_line[0] in b_names):
            b_names.append(l_line[0])
# Process each line in the file
    for line in inf_g:
        l_line = (line.rstrip()).split()
# Check if the name is already present
        if not(l_line[0] in g_names):
            g_names.append(l_line[0])
# Close the files
    inf_b.close()
    inf_g.close()
# Display the result
print("Names used for a boy:\n")
for name in b_names:
    print(name)
print("\nNames used for a girl:\n")
for name in g_names:
    print(name)