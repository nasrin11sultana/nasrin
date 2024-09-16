def factors(num):
    return [i for i in range(1, num+1) if num % i == 0]

num = int(input("Enter a number: "))
factors_list = factors(num)
print(f"Factors of {num}: {factors_list}")
