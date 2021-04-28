##
#Realize the tokenizing, the process of converting a string into a list 
#of substring, known as tokens
##Breaking the mathematical expression into a list of tokens
# @param m_e the mathematical expression
# @return the list of tokens
def tokenizing(m_e):
    t=[]
    i=0
    j=0
    while i<len(m_e):
        if m_e[i]=="/" or m_e[i]=="-" or m_e[i]=="^" or m_e[i]=="[" or m_e[i]=="]" or m_e[i]=="{" or m_e[i]=="}" \
or chr(40)<=m_e[i]<=chr(43):
            j=0
            t.append(m_e[i])
        elif chr(48)<=m_e[i]<=chr(57):
            if j==0:
                t.append(m_e[i])
                j=j+1
            else:
                t[len(t)-1]=t[len(t)-1]+m_e[i]
                j=j+1         
        i=i+1        
    return t
#Demonstrate the tokenizing function    
def main():
    math_expression=input("Enter a mathematical expression:\n")
    print("Tokens:\n",tokenizing(math_expression))
#Call the main function only if the file has not been imported into another program
if __name__=="__main__":
    main()                
