import math

def sphere_properties(radius):
    surface_area = 4 * math.pi * radius ** 2
    volume = (4/3) * math.pi * radius ** 3
    return surface_area, volume

# Example usage
r = float(input("Enter the radius of the sphere: "))
tsa, vol = sphere_properties(r)
print(f"Total Surface Area: {tsa:.2f} square units")
print(f"Volume: {vol:.2f} cubic units")
