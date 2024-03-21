def get_triangle_type(a, b, c):
    
    if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise IncorrectTriangleSides("Incorrect sides of a triangle")
    if a == b == c:
        return "equilateral"
    elif a == b or a == c or b == c:
        return "isosceles"
    else:
        return "nonequilateral"
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
