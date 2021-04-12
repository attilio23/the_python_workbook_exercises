#Display 15 approximations of pi greek
#Store the number of approximations as a constant
LIMIT=15
app=3.0
#Display the approximations of pi greek up to the limit
for i in range(LIMIT):
#Compute the approximations    
    app=app+4*((-1)**i/((2*i+2)*(2*i+3)*(2*i+4)))
#Display the result    
    print("Approximation  %2d of pi greek: %f"%(i+1,app))
