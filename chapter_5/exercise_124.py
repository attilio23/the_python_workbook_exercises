##
#Compute the line of best fit based on the points entered from the user
#Create two lists to store the x coordinates and the y coordinates
l_x=[]
l_y=[]
#Read the x coordinate from the user 
x=input("Enter the x coordinate:\n")
#Loop until x is a blank line
while(x!=""):
    l_x.append(float(x))
#Read the y coordinate from the user
    y=input("Enter the y coordinate:\n")
    l_y.append(float(y))
#Read the x coordinate from the user    
    x=input("Enter the x coordinate:\n")
#Check the number of items in the list     
if len(l_x)==0:
    print("The first x coordinate has not been inserted") 
elif len(l_x)==1:
    print("You must enter the coordinates of at least one point")   
else:
#Sum all the numbers of list l_x
    s_x=sum(l_x) 
#Sum all the numbers of list l_y   
    s_y=sum(l_y)
    s_x_y=0
    s_x_s=0
#For each element of l_x and l_y update the value of s_x_y and s_x_s   
    for i in range(len(l_x)):
        s_x_y=s_x_y+(l_x[i]*l_y[i])
        s_x_s=s_x_s+(l_x[i]**2)
#Compute m and b           
    m=(s_x_y-(s_x*s_y)/(len(l_x)))/(s_x_s-(s_x**2)/(len(l_x)))
    b=(s_y/len(l_y))-m*(s_x/len(l_x))
#Display the result     
    print("The line of best fit is:")
    print("y=%.2fx+%.2f"%(m,b)) 
