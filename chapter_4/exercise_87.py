##
#Calculate the shipping charge based on
#the number of products entered by the user
#Store the base rate and the variable rate as constants
BASE_RATE=10.95
VARIABLE_RATE=2.95
##Compute the shipping charge
#@param n_items the number of items
#@return the shipping charge
def compute_tot_shipping(n_items):
    if n_items==1:
        tot_shipping=BASE_RATE
    else:
        tot_shipping=BASE_RATE+(VARIABLE_RATE*(n_items-1))
    return tot_shipping
#Read from the user the number of items and display the shipping charge    
def main():
    n_i=int(input("Enter the number of items:\n"))
#Check if the number of items is valid    
    if n_i<1:
        print("The number of items entered isn't valid.\n")
    else:
        t_s=compute_tot_shipping(n_i)
        print("The shipping charge is:$%.2f ."%t_s)
#Call the main function        
main()                        