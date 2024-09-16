num = int(input("Enter a number: "))
difference = abs(num - 15)

if num > 15:
    result = 2 * difference
else:
    result = 4 * difference

print(f"Result: {result}")
