##
#Display the entire text of the song "The Twelve Days of Christmas"
from exercise_89 import determine_ord_number
#Store the upper limit and the lower limit as constants 
LOW_LIMIT=1
UPP_LIMIT=12
##Display a precise verse of the song
# @param n_verse the number of the verse
# @return (None)
def determine_verse(n_verse):
    print("On the %s day of Christmas"%(determine_ord_number(n_verse)))
    print("my true love sent to me:")
    if n_verse==12:
        print("Twelve drummers drumming,")
    if n_verse>=11:
        print("Eleven pipers piping,")    
    if n_verse>=10:
        print("Ten lords a-leaping,") 
    if n_verse>=9:
        print("Nine ladies dancing,")  
    if n_verse>=8:
        print("Eight maids a-milking,") 
    if n_verse>=7:
        print("Seven swans a-swimming,")
    if n_verse>=6:
        print("Six geese a-laying,") 
    if n_verse>=5:
        print("Five golden rings,") 
    if n_verse>=4:
        print("Four calling birds,") 
    if n_verse>=3:
        print("Three french hens,") 
    if n_verse>=2:
        print("Two turtle doves,") 
    if n_verse>1:
        print("And a partridge in a pear tree.")
    if n_verse==1:
        print("A partridge in a pear tree.") 
    print()    
#Display the song text           
def main():
#Display verses up to UPP_LIMIT    
    for i in range(LOW_LIMIT,UPP_LIMIT+1):
        determine_verse(i)
#Call the main function        
main()                                                   