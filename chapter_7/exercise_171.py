##
# Open a file and display it so that each line is as full as possible
# Store the maximum length as constant
MAX_LENGTH = 50
delimeter = " "
# Open the file for reading
inf = open("Alice’s_Adventures_in_Wonderland.txt", "r")
# Read the first line from the file
prev_line = inf.readline()
if prev_line == "":
    print("There is no text")
    quit()
prev_line = prev_line.rstrip()
p_l_l = prev_line.split()
# Read the next line from the file
next_line = inf.readline()
#  Keep looping until we have reached the end of the file 
while next_line != "":
    next_line = next_line.rstrip()
    n_l_l = next_line.split()
    if n_l_l:
        if len(prev_line) < MAX_LENGTH:
            while len(prev_line) < MAX_LENGTH and n_l_l:
                p_l_l.append(n_l_l.pop(0))
                prev_line = delimeter.join(p_l_l)
            if n_l_l:    
                if len(prev_line) > MAX_LENGTH:
                    n_l_l.insert(0, p_l_l.pop())
                prev_line = delimeter.join(p_l_l)
                print(prev_line)
                prev_line = delimeter.join(n_l_l)
                p_l_l = prev_line.split()
                next_line = inf.readline()
            else:
                next_line = inf.readline()       
        elif len(prev_line) > MAX_LENGTH:
            while len(prev_line) > MAX_LENGTH:
                n_l_l.insert(0, p_l_l.pop())
                prev_line = delimeter.join(p_l_l)
            print(prev_line)    
            prev_line = delimeter.join(n_l_l)
            p_l_l = prev_line.split()
            next_line = inf.readline()
        else:
            print(prev_line)
            prev_line = next_line
            p_l_l = prev_line.split()
            next_line = inf.readline() 
    else:
        if len(prev_line) <= MAX_LENGTH:
            print(prev_line)
        else:
            t_l = []
            while len(prev_line) > MAX_LENGTH:
                t_l.insert(0, p_l_l.pop())
                prev_line = delimeter.join(p_l_l)
                if len(prev_line) <= MAX_LENGTH:
                    print(prev_line)
                    prev_line = delimeter.join(t_l)
                    p_l_l = prev_line.split()
                    t_l = []
            print(prev_line)
        print("\r")
        prev_line = inf.readline()
        prev_line = prev_line.rstrip()
        p_l_l = prev_line.split()
        next_line = inf.readline()
# Check whether the length of the last line of text is less than or equal to the maximum length
if len(prev_line) <= MAX_LENGTH:
    print(prev_line)
else:
    t_l = []
    while len(prev_line) > MAX_LENGTH:
        t_l.insert(0, p_l_l.pop())
        prev_line = delimeter.join(p_l_l)
        if len(prev_line) <= MAX_LENGTH:
            print(prev_line)
            prev_line = delimeter.join(t_l)
            p_l_l = prev_line.split()
            t_l = []
    print(prev_line)           
# Close the file
inf.close()
print("\nEND")