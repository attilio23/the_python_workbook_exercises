## 
# Create a dictionary that maps from character to morse code
morse_code={".":".", "-":"-", "A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", \
"F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", \
"M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", \
"T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", \
"0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", \
"6":"-....", "7":"--...", "8":"---..", "9":"----."}
# Read a message from the user 
txt_message=input("Enter a text message:\n").upper()
# Create a string that will contain the message entered
# by the user translated into morse code
c_m_txt_message=""
# Translate each character of the message into morse code (if the character 
# does not represent a key of morse_code, ignore it)
for ch in txt_message:
    if ch in morse_code.keys():
        c_m_txt_message=c_m_txt_message+morse_code[ch]+" "
# Display the result        
print("The message in code morse is:\n",c_m_txt_message)    
