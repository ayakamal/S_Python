# Assignment 9
# 9- Ask the user to enter the radius of a circle i
# n order to alert its calculated area and circumference.

import math
def circle_area(r):
    area = math.pi * (r ** 2)
    print("The area of the circle is: "+ str(area))

def circle_circumference(r):
    circumference = 2 * math.pi * r
    print("The circumference of the circle is: " + str(circumference))

radius = float(input("Enter the radius of the circle: "))
circle_area(radius)
circle_circumference(radius)

