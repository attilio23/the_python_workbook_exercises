#reimbursement in respect of the measure
REIMB_UP_TO_1_L=0.10
REIMB_OVER_1_L=0.25
#number cointainers of one litre or less
n1=int(input("Enter the number of containers that measure a litre or less:\n"))
#number cointainers of more than one litre
n2=int(input("Enter the number of containers that measure more than one litre:\n"))
#calculating reimbursement
reimbursement=(n1*REIMB_UP_TO_1_L)+(n2*REIMB_OVER_1_L)
#print of the full reimbursement
print("Your full reimbursement is $%.2f" %reimbursement)        
