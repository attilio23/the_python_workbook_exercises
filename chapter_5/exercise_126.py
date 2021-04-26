##
#Simulate the distribution of cards 
from exercise_125 import createDeck, shuffle
#Store the number of hands and the number of cards per hand
NUM_HANDS=4
NUM_CARDS=5
##Deal the cards to players
# @param n_h the number of hands
# @param n_c the number of cards
# @param d_c the deck of cards
# @return the list containing all of the hands that were dealt 
def deal (n_h,n_c,d_c):
    l_hs=[] 
    for _ in range(n_h):
        l_hs.append([])     
    for _ in range(n_c):
        for i in range(len(l_hs)):
            l_hs[i].append(d_c[0])
            d_c.pop(0)
    return l_hs
#Demonstrate the deal function     
def main():
    deck_cards=createDeck()
    shuffle(deck_cards)
    l_hands=deal(NUM_HANDS,NUM_CARDS,deck_cards)
    print("All of the hands of cards:")
    print(l_hands)
    print("Remaining cards:")
    print(deck_cards) 
#Call the main function             
main()
