n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))

if n1<n2:
    greater=n2
else:
    greater=n1

while True:
    if (greater%n1==0) or (greater%n2==0):
        lcm=greater
        break
    greater+=1
print("The lcm is:",lcm)