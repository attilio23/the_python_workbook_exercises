##
#Generate a random licens plate
from random import randrange
#Store the maximum length, the minimum length, the maximum position 
#for letters, the minimum position for letters, the maximum position 
#for digits and the minimum position for digits as constants
MAX_L=7
MIN_L=6
MAX_P_L=90
MIN_P_L=65
MAX_P_D=57
MIN_P_D=48
#Generate the licens plate
# @return the random licens plate 
def randomLicensPlate():
#Initialize empty the random licens plate    
    l_p=""
#Determine the lenght of the licens plate    
    l=randrange(MIN_L,MAX_L+1)
    if l==MAX_L:
        for _ in range(l-3):
            l_p=l_p+chr(randrange(MIN_P_D,MAX_P_D+1))
        for _ in range(l-3,l):
            l_p=l_p+chr(randrange(MIN_P_L,MAX_P_L+1))
    else:
        for _ in range(l-3):
            l_p=l_p+chr(randrange(MIN_P_L,MAX_P_L+1))
        for _ in range(l-3,l):
            l_p=l_p+chr(randrange(MIN_P_D,MAX_P_D+1))
    return l_p  
#Demonstrate the randomLicensePlate      
def main():
    licens_plate=randomLicensPlate()
    print("Here the licens plate:%s"%licens_plate)
#Call the main function    
main()                




