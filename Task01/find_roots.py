import math

def find_roots(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return []
            else:
                return []
        else:
            return [-c / b]
    else:
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            return sorted([x1, x2])
        elif d == 0:
            x = -b / (2*a)
            return [x]
        else:
            return []
