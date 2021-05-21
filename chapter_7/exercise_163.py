##
# Read all the files in the baby names data set and identify all the 
# names that have been most popular in at least one year
# Store the first year and the last year as constants
FIRST_YEAR = 1900
LAST_YEAR = 2012
# Create two list to store the most popular names
p_n_b = []
p_n_g = []
# Process each year in the range
for l in range(FIRST_YEAR, LAST_YEAR + 1):
# Open the file for reading
    inf_b = open("BabyNames/"+str(l)+"_BoysNames.txt", "r")
    l_b = ((inf_b.readline()).rstrip()).split()
# Check if the name is already present in the list
    if not(l_b[0] in p_n_b):    
        p_n_b.append(l_b[0])
# Open the file for reading
    inf_g = open("BabyNames/"+str(l)+"_GirlsNames.txt", "r")
    l_g = ((inf_g.readline()).rstrip()).split()
# Check if the name is already present in the list
    if not(l_g[0] in p_n_g):
        p_n_g.append(l_g[0])
    inf_b.close()
    inf_g.close()
# Display the result
print("The most popular names for boys:\n")
for name in p_n_b:
    print(name)
# Display the result
print("\nThe most popular names for girls:\n")    
for name in p_n_g:
    print(name)    