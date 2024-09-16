def sum_and_average(a, b, c):
    total = a + b + c
    avg = total / 3
    return total, avg
num1 = float(input("Enter the first float number: "))
num2 = float(input("Enter the second float number: "))
num3 = float(input("Enter the third float number: "))
total, avg = sum_and_average(num1, num2, num3)
print(f"The sum of the numbers is: {total}")
print(f"The average of the numbers is: {avg}")
