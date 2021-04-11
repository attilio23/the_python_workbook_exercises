##
#Determine the corresponding note with respect to the frequency
C4=261.63
D4=293.66
E4=329.63
F4=349.23
G4=392.00
A4=440.00
B4=493.88
note=" "
#Read the frequency from the user
frequency=float(input("Enter the frequency(in Hertz):\n"))
if abs(frequency-A4)<1:
    note="A4"
elif abs(frequency-B4)<1:
    note="B4"
elif abs(frequency-C4)<1:
    note="C4"
elif abs(frequency-D4)<1:
    note="D4"
elif abs(frequency-E4)<1:
    note="E4"
elif abs(frequency-F4)<1:
    note="F4"
elif abs(frequency-G4)<1:
    note="G4"    
if note==" ":
    print("The frequency does not correspond to a known note")
else:
    print("The note corresponding to the inserted frequency is %s"%note)
