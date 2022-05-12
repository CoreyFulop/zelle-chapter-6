# triangle2_augmented.py

import math
from graphics import *

def square(x):
    return x * x

def distance(p1, p2):
    dist = math.sqrt(square(p2.getX() - p1.getX()) + square(p2.getY() - p1.getY()))
    return dist

def area(length1, length2, length3):
    s = (length1 + length2 + length3)/2
    return math.sqrt(s * (s - length1) * (s - length2) * (s - length3))

def main():
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)

    # Get and draw three vertices of triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)

    # Use Polygon object to draw the triangle
    triangle = Polygon(p1, p2, p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.draw(win)

    # Calculate the perimeter of the triangle
    perim = distance(p1, p2) + distance(p2, p3) + distance(p3, p1)
    message.setText(f"The perimeter is {round(perim, 2)}.")

    # Wait for mouse click to show area area data
    win.getMouse()

    # Calculate the area of the triangle
    dist1 = distance(p1, p2)
    dist2 = distance(p2, p3)
    dist3 = distance(p3, p1)
    triangle_area = area(dist1, dist2, dist3)
    message.setText(f"The area is {round(triangle_area, 2)}.")

    # Wait for another click to exit
    win.getMouse()
    win.close()

main()