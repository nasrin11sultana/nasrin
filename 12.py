a = float(input("Enter first side of the triangle: "))
b = float(input("Enter second side of the triangle: "))
c = float(input("Enter third side of the triangle: "))

if a == b == c:
    print("The triangle is equilateral.")
elif a == b or b == c or c == a:
    print("The triangle is isosceles.")
else:
    print("The triangle is scalene.")
