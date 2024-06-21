import math

def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

def further_from_origin(x1, y1, x2, y2):
    distance1 = distance_from_origin(x1, y1)
    distance2 = distance_from_origin(x2, y2)

    if distance1 < distance2:
        return "Point A is further from the origin."
    elif distance2 < distance1:
        return "Point B is further from the origin."
    else:
        return "Both points are at the same distance from the origin."

x1 = int(input("Enter x-coordinate of point A: "))
y1 = int(input("Enter y-coordinate of point A: "))
x2 = int(input("Enter x-coordinate of point B: "))
y2 = int(input("Enter y-coordinate of point B: "))

