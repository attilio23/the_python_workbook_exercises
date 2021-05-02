##
# Simulate 1000 rolls of two dice and display a table indicating the frequency 
# and percentage expected from the theory of probability for each total
from random import randrange
# Store the number of rolls as constant
NUM_ROLLS=1000
# Simulate 1000 rolls of two dice 
# @return the total that was rolled on two dice
def roll():
    d1=randrange(1,7)
    d2=randrange(1,7)
    return d1+d2  
# Display the table      
def main():
# Create a dictionary that maps from total to the frequency
    s_p_t={}
    for i in range(2,13):
        s_p_t[i]=0 
# Create a dictionary that maps from total to the percentage
# expected from the theory of probability    
    e_p_t={2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78} 
# Update the appropriate frequency for each roll
    for _ in range(NUM_ROLLS):
        t_r=roll()
        s_p_t[t_r]=s_p_t[t_r]+1
# Express the frequency for each total as a percentage of the number of rolls 
# performed         
    for t in s_p_t:
        s_p_t[t]=s_p_t[t]/10
# Display the result        
    print("Total  Simulated  Expected")
    print("         Percent   Percent")
    for i in range(2,13):
        print("%5d%11.2f%10.2f"%(i,s_p_t[i],e_p_t[i])) 
# Call the main function           
main()    