import unittest
from triangle_func import get_triangle_type
from incorrect_triangle_sides import IncorrectTriangleSides

class TestFunc(unittest.TestCase):
    def test_nonequilateral(self):
        self.assertEqual(get_triangle_type(4, 5, 6), "nonequilateral")
        
    def test_isosceles(self):
        self.assertEqual(get_triangle_type(3, 3, 4), "isosceles")
        
    def test_equilateral(self):
        self.assertEqual(get_triangle_type(6, 6, 6), "equilateral")

    def test_triangle_sides(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-4, 4, 3)

        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 2, 1)


if __name__ == '__main__':
    unittest.main()
