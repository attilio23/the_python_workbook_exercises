##
#Create a deck of cards, shuffle it and finally display the original deck of cards and the shuffled deck of cards
from random import randrange
#Store the number of cards as constant 
N=52
##Generate the deck of 52 cards
# @return the list in which the deck of cards is stored 
def createDeck():
    s_s="shdc"
    s_v="A23456789TJQK"
    d_c=[]
    for i in s_s:
        for j in s_v:
            d_c.append(j+i)
    return d_c
#Shuffle the deck of cards
# @param c the deck of cards
# @return (None)
def shuffle (c):
    t=""
    for i in range(len(c)):
        j=randrange(i,N)
        t=c[i]
        c[i]=c[j]
        c[j]=t
#Demonstrate the createDeck function and the shuffle function        
def main():
    deck_cards=createDeck()
    print("Here the original deck of cards:\n")
    print(deck_cards)
    shuffle(deck_cards)
    print("Here the original deck of cards after it has been shuffled:\n")
    print(deck_cards)
#Only call the main function when this file has not been imported     
if __name__=="__main__":
    main()        
