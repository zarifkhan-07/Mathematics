num=int(input("Enter the number:"))
result=0
temp=num
while temp!=0:
    digit=temp%10
    result=result+digit**3
    temp=temp//10
print(result)
if num==result:
    print("This a an armstrong number.")
else:
    print("This is not an armstrong number.")