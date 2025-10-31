nl=int(input("Enter the largest number:"))
ns=int(input("Enter the smallest number:"))

while ns:
    numstore=ns
    ns=nl%ns
    nl=numstore

print("HCF is:",nl)