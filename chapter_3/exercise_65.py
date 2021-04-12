##
#Display a table showing the conversion between degrees Celsius and degrees Fahrenheit
#Only consider Celsius temperatures between 0 and 100
for i in range(10, 101, 10):
    d_f=i*1.8+32
#Display the result   
    print("%3d degrees Celsius are equal to %3d degrees Fahrenheit ."%(i,d_f))
