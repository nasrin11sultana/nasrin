numbers = input("Enter comma-separated numbers: ")

# Generating list and tuple from input
num_list = numbers.split(',')
num_tuple = tuple(num_list)

print(f"List: {num_list}")
print(f"Tuple: {num_tuple}")
