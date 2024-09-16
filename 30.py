n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

largest_number = max(numbers)
print(f"The largest element in the list is: {largest_number}")
