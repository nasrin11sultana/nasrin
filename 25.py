def is_armstrong(num):
    num_str = str(num)
    power = len(num_str)
    return num == sum(int(digit) ** power for digit in num_str)

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
