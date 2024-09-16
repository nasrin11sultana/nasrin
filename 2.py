import math

def volume_of_sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = 6
volume = volume_of_sphere(radius)
print(f"Volume of the sphere: {volume:.2f} cm³")

