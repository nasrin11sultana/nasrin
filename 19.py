def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print(f"Sum of digits: {result}")
