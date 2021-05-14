##
# Perform the decompression of a list, which consists of replicating 
# each value in the list the number of times indicated
## Make the decompression of the list
# @param d_t_d the list to be decompressed
# @return the decompressed list
def decompression(d_t_d, i = 0):
# Base cases    
    if not(d_t_d):
        return d_t_d
    if i >= len(d_t_d):
        return d_t_d
# Recursive case            
    else:
        v = d_t_d[i] 
        n = d_t_d.pop(i+1) - 1
        for t in range(n):
            d_t_d.insert(i + 1, v)
        i = i + n + 1
        return decompression(d_t_d, i)   
# Demonstrate the decompression function        
def main():
    r_l_e_l = ["A", 12, "B", 4, "A", 6, "B", 1]
    print("Run-length encoded list:\n",r_l_e_l,"\n")   
    print("Decompression...\n",decompression(r_l_e_l))
# Call the main function
main()