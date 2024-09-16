def gravitational_force(m1, m2, distance, G=6.67430e-11):
    return G * (m1 * m2) / (distance ** 2)

m1 = float(input("Enter mass of first object (kg): "))
m2 = float(input("Enter mass of second object (kg): "))
d = float(input("Enter distance between the objects (m): "))

force = gravitational_force(m1, m2, d)
print(f"Gravitational Force: {force:.6e} N")
