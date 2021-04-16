##
#Center a string entered from the user in the terminal window
##Determine the spaces to achieve the centering
# @param string the string to center
# @param width the width of the terminal window
# @return the centered string
def center_string(string,width):
    new_string=string
    if len(string)<width:
        n_s=(width-len(string))//2
        new_string=" "*n_s+new_string
    return new_string
#Read the width of the window and strings to center from the user and
#demonstrate the center_string function    
def main():
    w=int(input("Enter the width of the terminal window:\n"))
    s1=input("Enter the first string:\n")
    s2=input("Enter the second string:\n")
    s3=input("Enter the third string:\n")
    print("Here are the strings centered in the terminal window:\n")
    print(center_string(s1,w))
    print(center_string(s2,w))
    print(center_string(s3,w))
#Call the main function    
main()