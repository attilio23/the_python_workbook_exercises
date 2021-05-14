##
# Implement the compression technique of a run-length inserted by the user
## Compress the run-length
# @param d_t_d the list to be compressed
# @return the compressed list
def coding(d_t_d, d_d = [], i = 0, j = 0):
# Base cases    
    if not(d_t_d):
        return d_d
    if i >= len(d_t_d):
        return d_d
# Recursive cases            
    if not(d_d) or d_t_d[i] != d_d[j]:
        if d_d:
            j = j + 2
        d_d.append(d_t_d[i])
        i = i + 1
        d_d.append(1)
        return coding(d_t_d, d_d, i, j)
    if d_t_d[i] == d_d[j]:
        d_d[-1] = d_d[-1] + 1
        i = i + 1
        return coding(d_t_d, d_d, i, j)
# Demonstrate the decoding function        
def main():
    delimeter = ","
    r_l_e_l = input("Enter the run-length:\n")
    print("Compression...\n",coding(r_l_e_l.split(delimeter)))
# Call the main function
main()    
       