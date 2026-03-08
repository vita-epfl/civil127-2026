# Solution for 4.1
# See https://github.com/vita-epfl/civil127-2026/blob/main/lab4/lab4.pdf

import math


def rope_length(x: float) -> float:
    """
    Calculate rope length as a function of x.


    alpha = PMA angle
    beta = AMB angle
    e = PA length
    """
    alpha = math.acos(1/x)
    beta = 2 * math.pi - math.pi/2 - 2 * alpha
    e = math.sqrt(x*x - 1)
    # since our angle is in radians and the radius 1, beta is also the arc length
    return 2 * (e + beta + 1)


def solve_x(L: float, accuracy: float) -> float:
    """
    Find a value for x using binary search. We are assuming rope_length() is
    monotonic from sqrt(2) onwards.
    """
    low = math.sqrt(2)
    high = L

    while True:
        mid = (low + high) / 2
        t = rope_length(mid)
        if abs(t - L) < accuracy:
            # stop when we are +/- accuracy with the desired length
            return mid
        if t > L:
            high = mid
        else:
            low = mid


rope = (math.pi * 2 + 4) * 1.000001
x = solve_x(rope, 0.00001)
print("x=", x)
