##
# Simulate the game Scrabble for a word entered from the user
# Create a dictionary that maps from letter to points 
l_p={"A":1, "E":1, "I":1, "L":1, "N":1, "O":1, "R":1, "S":1, "T":1, "U":1, \
"D":2, "G":2, "B":3, "C":3, "M":3, "P":3, "F":4, "H":4, "V":4, "W":4, "Y":4, \
"K":5, "J":8, "X":8, "Z":10, "Q":10}
score=0
# Read the word from the user
word=input("Enter the word:\n").upper()
# Update score for each loop
for ch in word:
    score=score+l_p[ch]
# Display the result    
print("The score is",score)