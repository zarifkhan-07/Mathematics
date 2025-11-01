for n in range(10, 100):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(end="")
            break
    else:
        print(n)
