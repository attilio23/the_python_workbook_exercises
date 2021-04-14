##
#Calculate the total fare based on the distance travelled entered by the user
#Store the base fare, the varible portion and the number of meters per chilometer as constants 
BASE_FARE=4.00  
VAR_PORTION=0.25
METERS_PER_CHILOMETER=1000
##Determine the total fare
#@param distance_travelled the distance travelled from the user
#@return the total fare 
def compute_tot_fare(distance_travelled):
    d_t_m=distance_travelled*METERS_PER_CHILOMETER
    t_f=BASE_FARE+(VAR_PORTION*(d_t_m//140))
    return t_f
#Demonstrate the compute_tot_fare function   
def main():
#Check if the distance travelled is valid    
    d_t=float(input("Enter the distance travelled(in kilometers):\n"))
    if d_t>0:    
        total_fare=compute_tot_fare(d_t)
        print("The total fare is:$%.2f"%total_fare)
    else:
        print("The distance travelled isn't valid.")    
#Call the main function    
main()        
    