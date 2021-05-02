##
# Create a dictionary that maps from key to character
num_keypad={1:[".", ",", "?", "!", ":"], 2:["A", "B", "C"], 3:["D", "E", "F"], \
4:["G", "H", "I"], 5:["J", "K", "L"], 6:["M", "N", "O"], 7:["P", "Q", "R", "S"], \
8:["T", "U", "V"], 9:["W", "X", "Y", "Z"], 0:" "}
# Read a text message from the user 
txt_message=input("Enter a text message:\n").upper()
# Create a string that will contain the sequence of 
# keys that must be pressed to realize the message
k_s_p=""
# Determine the sequence of keys for each character of the message
for ch in txt_message:
    if ch==num_keypad[0]:
        k_s_p=k_s_p+"0"
    else:
        f=0
        i=1
        while i<len(num_keypad) and f==0:
            if ch in num_keypad[i]:
                k_s_p=k_s_p+str(i)
                j=0
                while ch!=num_keypad[i][j]:
                    k_s_p=k_s_p+str(i)  
                    j=j+1 
                f=1  
            i=i+1        
#Display the result            
print("The sequence of keys that must be pressed to write the message is:\n",k_s_p)                        
