##
#Based on a specific list of values, count values greater or equal than a precise minimum 
#value and less than a precise maximum value
#Count values between minimum (included) and maximum (not included)
# @param v the list of values
# @param mn_v the minimum value
# @param mx_v the maximum value
# @return the number of values between the minimum (included) and the maximum (not included)
def countRange(v,mn_v,mx_v):
    count=0
    for i in v:
        if mn_v<=i<mx_v:
            count=count+1
    return count
#Demonstrate the countRange function    
def main():
    v1=[101,23,45,12,89,56,78,89,1,2]
    v2=[101,23,45,10,89,56,78,89,34,2]
    v3=[2.50,43,50,12,2.89,56,78,89.16,1,2]
    v4=[23,4,-2.5,35,0,89,-5,78,89,1,2]
    v5=[12.64,0.1,0.1,-27,8,56.9,7,9,1,2]
    v6=[1.9,2.6,6.8,6.8,6.7,6.9,7,89,1,2]
    v7=[1,5.90,5.99,5.999,7,0,7,21,10,36]
    v8=[]
    print("Values between 10 (included) and 33 (not included) in",v1,"are:",countRange(v1,10,33))
    print("Values between 30 (included) and 33 (not included) in",v1,"are:",countRange(v1,30,33))
    print("Values between 10 (included) and 40 (not included) in",v2,"are:",countRange(v2,10,40))
    print("Values between 12.50 (included) and 54.98 (not included) in",v3,"are:",countRange(v3,12.50,54.98))
    print("Values between -3 (included) and 15.35 (not included) in",v4,"are:",countRange(v4,-3,15.35))
    print("Values between 0 (included) and 12.64 (not included) in",v5,"are:",countRange(v5,0,12.64))
    print("Values between 6 (included) and 7 (not included) in",v6,"are:",countRange(v6,6,7))
    print("Values between 6 (included) and 7 (not included) in",v7,"are:",countRange(v7,6,7))
    print("Values between 6 (included) and 10 (not included) in",v8,"are:",countRange(v8,6,10))
#Call the main function
main()                
