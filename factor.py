def factors(number):
    print("The factors of",number,"are:")
    for i in range(1,num+1):
        if num%i==0:
            print(i)

num=int(input("Enter the number:"))
factors(num)