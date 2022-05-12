# pizza_again.py

import math 

def area_of_circle(radius):
    return math.pi * radius**2

def price_density(price, area):
    return price / area

def main():
    print("This program returns some data about a pizza.\n")

    price = eval(input("Please enter the price of the pizza: "))
    diameter = eval(input("Enter the diamater of the pizza: "))

    radius = diameter / 2

    pizza_area = area_of_circle(radius)
    area_cost = price_density(price, pizza_area)

    print(f"\nThe cost per square inch of this pizza is {round(area_cost, 2)}.")

main()