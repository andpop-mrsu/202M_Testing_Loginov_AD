import pytest
from triangle import Triangle
from incorrect_triangle_sides import IncorrectTriangleSides

def test_triangle_creation():
    triangle = Triangle(2, 3, 7)
    assert triangle.a == 2
    assert triangle.b == 3
    assert triangle.c == 7

    with pytest.raises(IncorrectTriangleSides):
        Triangle(-4, 4, 3)

    with pytest.raises(IncorrectTriangleSides):
        Triangle(0, 2, 1)
    
def test_triangle_type():

    first_tringle = Triangle(3, 3, 4)
    assert first_tringle.triangle_type() == "isosceles"

    second_tringle = Triangle(4, 5, 6)
    assert second_tringle.triangle_type() == "nonequilateral"

    third_triangle = Triangle(6, 6, 6)
    assert third_triangle.triangle_type() == "equilateral"


def test_triangle_perimeter():
    first_tringle = Triangle(5, 6, 7)
    assert first_tringle.perimeter() == 12

    second_tringle = Triangle(5, 5, 5)
    assert second_tringle.perimeter() == 15

    third_triangle = Triangle(4, 4, 3)
    assert third_triangle.perimeter() == 11

if __name__ == "__main__":
    pytest.main()
