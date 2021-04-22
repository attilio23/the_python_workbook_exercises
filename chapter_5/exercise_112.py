##
#Display the list of data of a science experiment without considering the outliers
#Store the number of maximum values and the number of minimum values 
#to be removed as constants
N=2
#Create a copy of the list of original values, removing outliers
# @param vls the list of the original values
# @param N the number of maximum and the number of minimum values to remove
# @return the list without outliers
def removeOutliers(vls,N):
    otlrs=sorted(vls) 
    for _ in range(N):
        otlrs.pop(0)     
        otlrs.pop()              
    return otlrs
#Demonstrate the removeOutliers function    
def main():
    values=[]
    v=int(input("Enter the first value:\n"))
#Keep looping while v is different from zero    
    while v!=0:
        values.append(v)
        v=int(input("Enter the value(0 to quit):\n"))
#Check if the number of original values is less than 4        
    if len(values)<4:
        print("The number of values can't be less than 4.")
    else:
        outliers=removeOutliers(values,N)
        print("Here the original values:\n",values)
        print("Here the original values without the outliers:\n",outliers)  
#Call the main function                  
main()    
