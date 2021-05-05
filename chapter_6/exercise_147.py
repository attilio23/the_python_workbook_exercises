##
# Determine whether a bingo card is winning
from exercise_146 import displayBingoCard, NMBRS_PER_CLMN
## Determine if a bingo card has a line of five numbers that have all been called
# @param b_c the bingo card
# @return True if b_c is a winning card. False otherwise
def isWinningCard(b_c):
    h_l=[[],[],[],[],[]]
    v_l=[]
    d1_l=[]
    d2_l=[]
    for k in b_c:
        v_l.append(b_c[k])
    for i in range(NMBRS_PER_CLMN):
        for j in v_l:
            c_l=j
            h_l[i].append(c_l[i])
    j=0        
    while j<len(v_l):
        d1_l.append(v_l[j][j])
        j=j+1
    j=len(v_l)-1
    i=0
    while j>=0:
        d2_l.append(v_l[j][i])
        j=j-1  
        i=i+1
    if sum(d1_l)==0:
        return True
    if sum(d2_l)==0:
        return True
    for i in v_l:
        if sum(i)==0:
            return True
    for i in h_l:
        if sum(i)==0:
            return True
    return False   
# Demonstrate the isWinningCard function                                     
def main():
    bingo_card1={"B":[7, 10, 13, 1, 5], "I":[16, 20, 25, 30, 29], "N":[0, 0, 0, 0, 0], "G":[48, 59, 50, 54, 49], "O":[62, 75, 63, 73, 71]}
    bingo_card2={"B":[7, 10, 0, 1, 5], "I":[16, 20, 0, 30, 29], "N":[35, 41, 0, 40, 44], "G":[48, 59, 0, 54, 49], "O":[62, 75, 0, 73, 71]}
    bingo_card3={"B":[7, 10, 13, 1, 0], "I":[16, 20, 25, 0, 29], "N":[35, 41, 0, 40, 44], "G":[48, 0, 50, 54, 49], "O":[0, 75, 63, 73, 71]}
    bingo_card4={"B":[0, 10, 13, 1, 5], "I":[16, 0, 25, 30, 29], "N":[35, 41, 0, 40, 44], "G":[48, 59, 50, 0, 49], "O":[62, 75, 63, 73, 0]}
    bingo_card5={"B":[7, 10, 13, 1, 5], "I":[16, 20, 25, 30, 29], "N":[35, 41, 36, 40, 44], "G":[48, 59, 50, 54, 49], "O":[62, 75, 63, 73, 71]}
    bingo_card6={"B":[7, 0, 13, 1, 5], "I":[16, 20, 25, 30, 0], "N":[35, 0, 36, 40, 44], "G":[0, 59, 50, 54, 49], "O":[62, 0, 63, 73, 71]}
    bingo_card7={"B":[7, 10, 13, 1, 5], "I":[16, 20, 25, 30, 29], "N":[0, 0, 0, 0, 44], "G":[48, 59, 50, 54, 49], "O":[62, 75, 0, 73, 71]}
    print("  BINGO CARD 1  ")
    displayBingoCard(bingo_card1)
    if isWinningCard(bingo_card1):
        print("Bingo Card 1 is winning.\n")
    else:
        print("Bingo Card 1 isn't winning.\n")
    print("  BINGO CARD 2  ")
    displayBingoCard(bingo_card2)
    if isWinningCard(bingo_card2):
        print("Bingo Card 2 is winning.\n")
    else:
        print("Bingo Card 2 isn't winning.\n")  
    print("  BINGO CARD 3  ")
    displayBingoCard(bingo_card3)
    if isWinningCard(bingo_card3):
        print("Bingo Card 3 is winning.\n")
    else:
        print("Bingo Card 3 isn't winning.\n") 
    print("  BINGO CARD 4  ")
    displayBingoCard(bingo_card4)
    if isWinningCard(bingo_card4):
        print("Bingo Card 4 is winning.\n")
    else:
        print("Bingo Card 4 isn't winning.\n")
    print("  BINGO CARD 5  ")
    displayBingoCard(bingo_card5)
    if isWinningCard(bingo_card5):
        print("Bingo Card 5 is winning.\n")
    else:
        print("Bingo Card 5 isn't winning.\n") 
    print("  BINGO CARD 6  ")
    displayBingoCard(bingo_card6)
    if isWinningCard(bingo_card6):
        print("Bingo Card 6 is winning.\n")
    else:
        print("Bingo Card 6 isn't winning.\n") 
    print("  BINGO CARD 7  ")
    displayBingoCard(bingo_card7)
    if isWinningCard(bingo_card7):
        print("Bingo Card 7 is winning.\n")
    else:
        print("Bingo Card 7 isn't winning.\n") 
#Only call the main function when this file has not been imported          
if __name__=="__main__":
    main()
