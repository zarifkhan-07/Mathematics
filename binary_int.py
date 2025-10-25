# Convert binary to decimal manually
binary = input("Enter a binary number: ")
decimal = 0
power = 0

for digit in binary[::-1]:  # Start from rightmost bit
    if digit == '1':
        decimal += 2 ** power
    power += 1

print("The decimal value is:", decimal)
