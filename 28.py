n = int(input("Enter number of elements: "))
user_list = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    user_list.append(element)

print("The entered list is:", user_list)
