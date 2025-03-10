from math import pi


def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(h, (int,float)):
        if a >= 0 and b >= 0 and h >= 0:
            return 0.5 * (a + b) * h
        else:
            raise ValueError("Invalid Range: Please enter values greater than 0 or 0")
    else:
        raise ValueError("Invalid Value: Please enter a Integer or Float")

def ellipse_area(a, b):
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        if a >= 0 and b >= 0:
            return pi * a * b
        else:
            raise ValueError("Invalid Range: Please enter values greater then 0 or 0")
    else:
        raise ValueError("Invalid Value: Please enter a Integer or Float")

def rhombus_area(d1, d2):
    if isinstance(d1, (int,float)) and isinstance(d2, (int,float)):
        if d1 >= 0 and d2 >= 0:
            return 0.5 * d1 * d2
        else:
            raise ValueError("Invalid Range: Please enter values greater than 0 or 0")
    else:
        raise ValueError("Invalid Value: Please enter a Integer or Float")