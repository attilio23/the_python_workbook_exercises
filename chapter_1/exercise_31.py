##
#Conversion from kilopascals to pounds per square inch, millimeters of mercury and atmospheres
KIL_PER_PPSI=6.89476
KIL_PER_ATM=101.325
MOM_PER_KIL=7.50062
#Read the pressure from the user
pressure_KIL=float(input("Enter the pressure in kilopascals :\n"))
#Compute the equivalent pressure in pounds per square inch, millimeters of mercury and atmospheres
pressure_PPSI=pressure_KIL/KIL_PER_PPSI
pressure_ATM=pressure_KIL/KIL_PER_ATM
pressure_MOM=pressure_KIL*MOM_PER_KIL
#Display the result
print("%.3f kilopascals are equivalent to %.3f pounds per square inch, %.3f millimeters of mercury and %.3f atmospheres "%(pressure_KIL,pressure_PPSI,pressure_MOM,pressure_ATM))
