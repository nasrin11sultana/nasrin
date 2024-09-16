n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

average = sum(numbers) / n
print(f"The average of the numbers is: {average}")
