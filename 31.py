def linear_search(lst, key):
    for index, element in enumerate(lst):
        if element == key:
            return index
    return -1

n = int(input("Enter the number of elements: "))
lst = []

for i in range(n):
    element = input(f"Enter element {i + 1}: ")
    lst.append(element)

key = input("Enter the element to search for: ")

result = linear_search(lst, key)
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the list")
