import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import unittest
import circle
import math


class TestCircle(unittest.TestCase):

    def test_area_normal(self):
        self.assertAlmostEqual(circle.area(9), 254.46900494077323, places=10)
        self.assertAlmostEqual(circle.area(1), math.pi, places=10)
        self.assertEqual(circle.area(2), 4 * math.pi)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(circle.perimeter(9), 56.54866776461627, places=10)
        self.assertAlmostEqual(circle.perimeter(1), 2 * math.pi, places=10)

    def test_float_values(self):
        self.assertAlmostEqual(circle.area(2.5), math.pi * 2.5 * 2.5, places=10)
        self.assertAlmostEqual(circle.perimeter(2.5), 5 * math.pi, places=10)

    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_area_negative(self):
        self.assertEqual(circle.area(-5), math.pi * 25)

    def test_perimeter_negative(self):
        self.assertEqual(circle.perimeter(-5), -10 * math.pi)

    def test_area_large_number(self):
        self.assertAlmostEqual(circle.area(1000), math.pi * 1000000, places=5)

    def test_perimeter_large_number(self):
        self.assertAlmostEqual(circle.perimeter(1000), 2000 * math.pi, places=5)

    def test_area_small_fraction(self):
        self.assertAlmostEqual(circle.area(0.001), math.pi * 0.000001, places=15)

    def test_perimeter_small_fraction(self):
        self.assertAlmostEqual(circle.perimeter(0.001), 0.002 * math.pi, places=15)

    def test_area_one(self):
        self.assertEqual(circle.area(1), math.pi)

    def test_perimeter_one(self):
        self.assertEqual(circle.perimeter(1), 2 * math.pi)

    def test_area_half(self):
        self.assertAlmostEqual(circle.area(0.5), math.pi * 0.25, places=10)

    def test_perimeter_half(self):
        self.assertAlmostEqual(circle.perimeter(0.5), math.pi, places=10)

    def test_area_ten(self):
        self.assertEqual(circle.area(10), 100 * math.pi)

    def test_perimeter_ten(self):
        self.assertEqual(circle.perimeter(10), 20 * math.pi)

    def test_area_negative_fraction(self):
        self.assertEqual(circle.area(-2.5), math.pi * 6.25)

    def test_perimeter_negative_fraction(self):
        self.assertEqual(circle.perimeter(-2.5), -5 * math.pi)

    def test_area_square_relation(self):
        r = 7
        area = circle.area(r)
        self.assertAlmostEqual(math.sqrt(area / math.pi), r, places=10)

    def test_perimeter_area_relation(self):
        r = 4
        perimeter = circle.perimeter(r)
        area = circle.area(r)
        self.assertAlmostEqual(perimeter, 2 * math.sqrt(math.pi * area), places=10)

    def test_area_float_precision(self):
        r = 3.14159
        expected = math.pi * r * r
        self.assertAlmostEqual(circle.area(r), expected, places=10)

    def test_perimeter_float_precision(self):
        r = 3.14159
        expected = 2 * math.pi * r
        self.assertAlmostEqual(circle.perimeter(r), expected, places=10)

    def test_area_very_small(self):
        r = 1e-10
        expected = math.pi * 1e-20
        self.assertAlmostEqual(circle.area(r), expected, places=25)

    def test_perimeter_very_small(self):
        r = 1e-10
        expected = 2 * math.pi * 1e-10
        self.assertAlmostEqual(circle.perimeter(r), expected, places=25)

    def test_area_very_large(self):
        r = 1e6
        expected = math.pi * 1e12
        self.assertAlmostEqual(circle.area(r), expected, places=5)

    def test_perimeter_very_large(self):
        r = 1e6
        expected = 2 * math.pi * 1e6
        self.assertAlmostEqual(circle.perimeter(r), expected, places=5)

    def test_area_pi(self):
        self.assertAlmostEqual(circle.area(math.pi), math.pi ** 3, places=10)

    def test_perimeter_pi(self):
        self.assertAlmostEqual(circle.perimeter(math.pi), 2 * math.pi ** 2, places=10)

    def test_area_int_and_float(self):
        self.assertEqual(circle.area(3), circle.area(3.0))

    def test_perimeter_int_and_float(self):
        self.assertEqual(circle.perimeter(3), circle.perimeter(3.0))

    def test_area_negative_zero(self):
        self.assertEqual(circle.area(-0), 0)

    def test_perimeter_negative_zero(self):
        self.assertEqual(circle.perimeter(-0), 0)

    def test_area_sequence(self):
        for r in [1, 2, 3, 4, 5]:
            expected = 2 * math.pi * r
            self.assertEqual(circle.perimeter(r), expected)

    def test_area_symmetry(self):
        r = 5
        self.assertEqual(circle.area(r), circle.area(-r))

    def test_perimeter_antisymmetry(self):
        r = 5
        self.assertEqual(circle.perimeter(r), -circle.perimeter(-r))

if __name__ == '__main__':
    unittest.main(verbosity=2)
