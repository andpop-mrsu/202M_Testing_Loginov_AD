class Triangle:
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or b + c <= a or a + c <= b:
            raise IncorrectTriangleSides("Incorrect sides of a triangle")
        self.a = a
        self.b = b
        self.c = c

    def triangle_type(self):
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return "isosceles"
        elif self.a == self.b == self.c:
            return "equilateral"
        else:
            return "nonequilateral"

    def perimeter(self):
        return self.a + self.b + self.c
