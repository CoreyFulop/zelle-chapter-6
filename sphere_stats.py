# sphere_stats.py

import math

def sphereArea(radius):
    return 4 * math.pi * radius**2

def sphereVolume(radius):
    return (4/3) * math.pi * radius**3

def main():
    print("This program returns some information about a sphere, given its radius.\n")

    radius = eval(input("Enter the radius: "))

    area = sphereArea(radius)
    volume = sphereVolume(radius)

    print(f"\nThe surface area is {round(area, 2)} and the volume is {round(volume, 2)}.")

main()