##
#Determine if the three sides entered from the user can be sides of a triangle
#Determine if it is a tringle
# @param side_1 the first side 
# @param side_2 the second side
# @param side_3 the third side
# @return True if it is a triangle. False otherwise.
def is_a_triangle(side_1,side_2,side_3):
    if side_1<=0 or side_2<=0 or \
side_3<=0 or side_1>=side_2+side_3 or \
side_2>=side_1+side_3 or side_3>=side_1+side_2:
        return False
    else:
        return True 
#Demonstrate the is_a_triangle function        
def main():
    s_1=float(input("Enter the first side:\n"))
    s_2=float(input("Enter the second side:\n"))
    s_3=float(input("Enter the third side:\n")) 
    if is_a_triangle(s_1,s_2,s_3):
        print("It is a tringle.")
    else:
        print("It isn't a tringle.")
#Call the main function        
main()                         