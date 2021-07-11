import math


def solve_quadratic(a,b,c):
    # https://www.youtube.com/watch?v=VOXYMRcWbF8
    if a == 0:
        return None
    
    inner = b**2 - 4*a*c
    if inner < 0:
        return None # only solve for real_number solutions
    
    pos = (-b + math.sqrt(inner)) / 2 * a
    neg = (-b - math.sqrt(inner)) / 2 * a

    if pos == neg:
        return pos

    return (pos, neg)

print(solve_quadratic(1,8,8))