##
#Perform encryption and decryption of messages
#Read the shift amount and the message from the user
message=input("Enter the message:\n")
shift_amount=int(input("Enter the shift amount:\n"))
new_message=""
#Check if the user wants to perform encryption or decryption
if shift_amount>0:
#Encrypt each character until the end of the message    
    for i in message:
        if 65<=ord(i)<=90-shift_amount or 97<=ord(i)<=122-shift_amount:
            new_message=new_message+chr(ord(i)+shift_amount)
        elif 90-shift_amount+1<=ord(i)<=90:
            new_message=new_message+chr(64+shift_amount-(90-ord(i)))
        elif 122-shift_amount+1<=ord(i)<=122:
            new_message=new_message+chr(96+shift_amount-(122-ord(i))) 
        else:
            new_message=new_message+i 
#Display the result                   
    print("The new message is :\n%s"%new_message) 
elif shift_amount<0:
#Dencrypt each character until the end of the message
    for i in message:
        if 65-shift_amount<=ord(i)<=90 or 97-shift_amount<=ord(i)<=122:
            new_message=new_message+chr(ord(i)+shift_amount)
        elif 65<=ord(i)<=65-shift_amount-1:
            new_message=new_message+chr(91-(-shift_amount-(ord(i)-65)))
        elif 97<=ord(i)<=97-shift_amount-1:
            new_message=new_message+chr(123-(-shift_amount-(ord(i)-97))) 
        else:
            new_message=new_message+i  
#Display the result                     
    print("The new message is :\n%s"%new_message)               
else:
    print("The shift amount entered isn't valid .")