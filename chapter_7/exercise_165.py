##
# Use the baby names data set to determine which names were used most often within
# a time period
try:
# Read the first year from the user
    first_year = int(input("Enter the first year:\n"))
# Read the last year from the user
    last_year = int(input("Enter the last year:\n"))
# Check if the first and last years are equal
    if first_year != last_year:
# Create a dictionary that maps from male names to the number of times they have been used 
        b_n_f = {}
# Create a dictionary that maps from female names to the number of times they have been used
        g_n_f = {}
# Process each year in the range
        for year in range(first_year, last_year + 1):
# Open the file for reading
            inf_b = open("BabyNames/"+str(year)+"_BoysNames.txt", "r")
# Open the file for reading
            inf_g = open("BabyNames/"+str(year)+"_GirlsNames.txt", "r")
# Process each line in the file
            for line in inf_b:
                l_b_names = (line.rstrip()).split()
# Check if the name is already in the dictionary keys
                if l_b_names[0] in b_n_f.keys():
                    b_n_f[l_b_names[0]] = b_n_f[l_b_names[0]] + int(l_b_names[1])
                else:
                    b_n_f[l_b_names[0]] = int(l_b_names[1])    
# Process each line in the file
            for line in inf_g:
                l_g_names = (line.rstrip()).split()
# Check if the name is already in the dictionary keys
                if l_g_names[0] in g_n_f.keys():
                    g_n_f[l_g_names[0]] = g_n_f[l_g_names[0]] + int(l_g_names[1])
                else:
                    g_n_f[l_g_names[0]] = int(l_g_names[1])                         
# Close the files
            inf_b.close()
            inf_g.close()           
# Determine the maximum value
        mx_b_v = max(b_n_f.values())
# Determine the maximum value        
        mx_g_v = max(g_n_f.values())       
# Display the result
        print("Most used male name between %d and %d:\n"%(first_year, last_year))
        for k in b_n_f:
            if b_n_f[k] == mx_b_v:
                print(k)
# Display the result
        print("Most used female name between %d and %d:\n"%(first_year, last_year))
        for k in g_n_f:
            if g_n_f[k] == mx_g_v:
                print(k)        
    else:
        print("Non devi inserire lo stesso anno")
except:
# Display an error message if user enters invalid input
    print("Devono essere inseriti anni compresi tra il 1900 e il 2012")