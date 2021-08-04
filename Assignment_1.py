# Assignment 1
# 1- Given two points represented as x1,y1,x2,y2.
# Return the (float) distance between them
# considering the following distance equation.

import math
def distance_eqn(x1, x2, y1, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return distance


d1 = 5.3
d2 = 6.5
h1 = 3.7
h2 = 2.6
distance = distance_eqn(d1, d2, h1, h2)
print(distance)
