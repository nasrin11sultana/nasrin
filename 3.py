import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"Area of the circle: {area:.2f} square units")

