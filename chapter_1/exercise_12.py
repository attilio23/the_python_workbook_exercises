##
#Compute the distance between two points on the surface of the Earth
import math
AVERAGE_RADIUS_EARTH=6371.01
#Read the latitude and the longitude of the two points from the user
t_1=float(input("Enter the latitude of the first point in degrees:\n"))  
g_1=float(input("Enter the longitude of the first point in degrees:\n"))
t_2=float(input("Enter the latitude of the second point in degrees:\n"))
g_2=float(input("Enter the longitude of the second point in degrees:\n"))
if (t_1==t_2) and (g_1==g_2):
    print("The two points coincide!")
else:
    #Conversion from degrees to radians
    t_1=math.radians(t_1)
    g_1=math.radians(g_1)
    t_2=math.radians(t_2)
    g_2=math.radians(g_2)
    #Compute the distance
    distance=AVERAGE_RADIUS_EARTH*math.acos(math.sin(t_1)*math.sin(t_2)+math.cos(t_1)*math.cos(t_2)*math.cos(g_1-g_2))
    #Display the result
    print("The distance between the points is: %.3f kilometers"%distance)
    #Conversion from degrees to radians
                            
                             
