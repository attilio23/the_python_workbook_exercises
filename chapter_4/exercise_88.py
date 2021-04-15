##
#Compute the median base on three numbers entered from the user
##Compute the median
#@param number_1 the first number
#@param number_2 the second number 
#@param number_3 the third number
#@return the median
def compute_median(number_1,number_2,number_3):
    mx=max(number_1,number_2,number_3)
    mn=min(number_1,number_2,number_3)
    med=(number_1+number_2+number_3)-(mx+mn)
    return med
#Read the three numbers from the user and display the median    
def main():
    n_1=int(input("Enter the first number:\n"))
    n_2=int(input("Enter the second number:\n"))
    n_3=int(input("Enter the third number:\n"))  
    median=compute_median(n_1,n_2,n_3)
    print("The median is",median)
#Call the main function    
main()      