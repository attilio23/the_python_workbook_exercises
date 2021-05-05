##
# Simulate a game of Bingo for a single card
from exercise_146 import generateBingoCard, displayBingoCard, NMBRS_PER_CLMN
from exercise_147 import isWinningCard
import random
# Store the maximum and minimum call as constants 
MN_NUM=1
MX_NUM=75
# Store the maximum number of games as constant
MX_NUM_GAMES=1000
# Create a Bingo Card
bingo_card=generateBingoCard()
# Create a list that stores the number of calls
# needed before the card wins for each game
gs_c=[]
# Create a list that stores the keys of bingo_card
k_b_c=[]
for k in bingo_card:
    k_b_c.append(k)
# Create a list that stores a copy of the original Bingo Card for each game    
ds_l=[]
for ds_l_i in range(MX_NUM_GAMES):
    ds_l.append({})  
for dictionary in ds_l:
    for i in range(len(k_b_c)):
        dictionary[k_b_c[i]]=[]
for dictionary in ds_l:
    for i in range(len(k_b_c)):
        numbers=bingo_card[k_b_c[i]]
        for number in numbers:
            dictionary[k_b_c[i]].append(number)              
ds_l_i=0
# Simulate the games    
for g in range(MX_NUM_GAMES):
# Create a list that stores all the calls of the game    
    bingo_calls=[]
    for c in range(MN_NUM, MX_NUM+1):
        bingo_calls.append(c)
    random.shuffle(bingo_calls)
    b_cs_i=0
# Keep looping while the card is not winning and b_cs_i is less than the length 
# of bingo_calls   
    while not(isWinningCard(ds_l[ds_l_i])) and b_cs_i<len(bingo_calls):
        b_cd_i=0
        f=0
# Keep looping while b_cs_i is less than the length of the current Bingo Card and 
# the call has not yet been found in the current Bingo Card       
        while b_cd_i<len(ds_l[ds_l_i]) and f==0:
            if bingo_calls[b_cs_i] in ds_l[ds_l_i][k_b_c[b_cd_i]]:
                i=0
                while i<len(ds_l[ds_l_i][k_b_c[b_cd_i]]) and f==0:
                    if ds_l[ds_l_i][k_b_c[b_cd_i]][i]==bingo_calls[b_cs_i]:
                        ds_l[ds_l_i][k_b_c[b_cd_i]][i]=0
                        f=1
                    i=i+1    
            b_cd_i=b_cd_i+1
        b_cs_i=b_cs_i+1  
    gs_c.append(b_cs_i)
    ds_l_i=ds_l_i+1   
gs_c.sort()
# Display the result
print("The minimum number of calls that must be made before the card wins is %d"%gs_c[0])
print("The maximum number of calls that must be made before the card wins is %d"%gs_c[-1])
print("The average number of calls that must be made before the card wins is %.2f"%(sum(gs_c)/MX_NUM_GAMES))
        