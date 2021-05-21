##
# Convert from letter grades to grade points and vice-versa
# Read the first value from the user
g = input("Enter the value:\n")
# Keep looping while the user enter a non-blank line
while g:
    try:
        g_p_1 = float(g)
        if g_p_1 > 4.0:
            l_g_1 = "A+"
        elif 3.85 <= g_p_1 <= 4.0:
            l_g_1 = "A"
        elif 3.5 <= g_p_1 < 3.85:
            l_g_1 = "A-"
        elif 3.15 <= g_p_1 < 3.50:
            l_g_1 = "B+"    
        elif 3.0 <= g_p_1 < 3.15:
            l_g_1 = "B"
        elif 2.5 <= g_p_1 < 2.85:
            l_g_1 = "B-"
        elif 2.15 <= g_p_1 < 2.5:
            l_g_1 = "C+"
        elif 1.85 <= g_p_1 < 2.15:
            l_g_1 = "C"
        elif 1.5 <= g_p_1 < 1.85:
            l_g_1 = "C-"
        elif 1.15 <= g_p_1 < 1.5:
            l_g_1 = "D+"        
        elif 0.5 <= g_p_1 < 1.15:
            l_g_1 = "D"
        elif g_p_1 < 0.5:
            l_g_1 = "F"
# Display the result       
        print("Conversion:",l_g_1)          
    except ValueError:
        try:
            l_g_2 = g
            if (l_g_2 == "A+") or (l_g_2 == "A"):
                g_p_2 = 4.0
            elif l_g_2 == "A-":
                g_p_2 = 3.7
            elif l_g_2 == "B+":
                g_p_2 = 3.3
            elif l_g_2 == "B":
                g_p_2 = 3.0
            elif l_g_2 == "B-":
                g_p_2 = 2.7
            elif l_g_2 == "C+":
                g_p_2 = 2.3
            elif l_g_2 == "C":
                g_p_2 = 2.0
            elif l_g_2 == "C-":
                g_p_2 = 1.7
            elif l_g_2 == "D+":
                g_p_2 = 1.3
            elif l_g_2 == "D":#ciao
                g_p_2 = 1.0
            elif l_g_2 == "F":
                g_p_2 = 0
# Display the result
            print("Conversion:",g_p_2)
# Totally remove the definition for g_p_2
            del g_p_2    
        except NameError:
# Indicate that the input provided is invalid if both conversions fail
            print("Invalid input\n")        
# Read the value from the user
    g = input("Enter the value(blank to quit):\n")   
print("END")