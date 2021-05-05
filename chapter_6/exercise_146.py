##
# Generate and display a Bingo Card
from random import randrange
# Store the number of numbers per column as constant
NMBRS_PER_CLMN=5
# Generate a Bingo Card
# @return the dictionary representing the Bingo Card 
def generateBingoCard():  
    b_c={"B":[], "I":[], "N":[], "G":[], "O":[]}
    i=1
    j=15
    for k in b_c:
        for _ in range(NMBRS_PER_CLMN):
            n=randrange(i,j+1)
            while n in b_c[k]:
                n=randrange(i, j+1)
            b_c[k].append(n) 
        i=j+1
        j=j+15      
    return b_c
## Display the Bingo Card
# @param bingo_card the Bingo Card
# @return (None)
def displayBingoCard(bingo_card):
    cs_l=[]
    for k in bingo_card:
        cs_l.append(bingo_card[k])  
    for i in range(NMBRS_PER_CLMN):
        for j in cs_l:
            c_l=j
            print("%3d"%c_l[i],end='') 
        print("\t") 
#Demonstrate the generateBingoCard function and the displayBingoCard function                
def main():
    print("   BINGO CARD  ")
    displayBingoCard(generateBingoCard())
#Only call the main function when this file has not been imported            
if __name__=="__main__":
    main()    