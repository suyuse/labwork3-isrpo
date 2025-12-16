import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import unittest
import square


class TestSquare(unittest.TestCase):

    def test_area_normal(self):
        self.assertEqual(square.area(2), 4)
        self.assertEqual(square.area(5), 25)
        self.assertEqual(square.area(2.5), 6.25)

    def test_perimeter_normal(self):
        self.assertEqual(square.perimeter(2), 8)
        self.assertEqual(square.perimeter(5), 20)
        self.assertEqual(square.perimeter(2.5), 10.0)

    def test_large_values(self):
        self.assertEqual(square.area(1000), 1000000)
        self.assertEqual(square.perimeter(1000), 4000)

    def test_area_zero_side(self):
        self.assertEqual(square.area(0), 0)

    def test_perimeter_zero_side(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_area_negative_side(self):
        self.assertEqual(square.area(-5), 25)

    def test_perimeter_negative_side(self):
        self.assertEqual(square.perimeter(-5), -20)

    def test_area_one(self):
        self.assertEqual(square.area(1), 1)

    def test_perimeter_one(self):
        self.assertEqual(square.perimeter(1), 4)

    def test_area_ten(self):
        self.assertEqual(square.area(10), 100)

    def test_perimeter_ten(self):
        self.assertEqual(square.perimeter(10), 40)

    def test_area_hundred(self):
        self.assertEqual(square.area(100), 10000)

    def test_perimeter_hundred(self):
        self.assertEqual(square.perimeter(100), 400)

    def test_perimeter_small_fraction(self):
        self.assertEqual(square.perimeter(0.1), 0.4)

    def test_area_very_small(self):
        self.assertEqual(square.area(0.001), 0.000001)

    def test_perimeter_very_small(self):
        self.assertEqual(square.perimeter(0.001), 0.004)

    def test_area_very_large(self):
        self.assertEqual(square.area(1000000), 1000000000000)

    def test_perimeter_very_large(self):
        self.assertEqual(square.perimeter(1000000), 4000000)

    def test_area_negative_fraction(self):
        self.assertEqual(square.area(-2.5), 6.25)

    def test_perimeter_negative_fraction(self):
        self.assertEqual(square.perimeter(-2.5), -10)

    def test_area_int_and_float(self):
        self.assertEqual(square.area(3), square.area(3.0))

    def test_perimeter_int_and_float(self):
        self.assertEqual(square.perimeter(3), square.perimeter(3.0))

    def test_area_negative_zero(self):
        self.assertEqual(square.area(-0), 0)

    def test_perimeter_negative_zero(self):
        self.assertEqual(square.perimeter(-0), 0)

    def test_area_sequence(self):
        for a in [1, 2, 3, 4, 5]:
            self.assertEqual(square.area(a), a * a)

    def test_perimeter_sequence(self):
        for a in [1, 2, 3, 4, 5]:
            self.assertEqual(square.perimeter(a), 4 * a)

    def test_area_symmetry(self):
        a = 5
        self.assertEqual(square.area(a), square.area(-a))

    def test_perimeter_antisymmetry(self):
        a = 5
        self.assertEqual(square.perimeter(a), -square.perimeter(-a))

    def test_area_perimeter_relation(self):
        a = 7
        area = square.area(a)
        perimeter = square.perimeter(a)
        self.assertEqual(perimeter, 4 * (area ** 0.5))

    def test_area_square_of_perimeter(self):
        a = 3
        perimeter = square.perimeter(a)
        self.assertEqual(square.area(a), (perimeter / 4) ** 2)

    def test_area_multiples(self):
        self.assertEqual(square.area(2), 4 * square.area(1))
        self.assertEqual(square.area(4), 16 * square.area(1))

    def test_perimeter_multiples(self):
        self.assertEqual(square.perimeter(2), 2 * square.perimeter(1))
        self.assertEqual(square.perimeter(4), 4 * square.perimeter(1))

    def test_area_double_side(self):
        self.assertEqual(square.area(6), 4 * square.area(3))

    def test_perimeter_double_side(self):
        self.assertEqual(square.perimeter(6), 2 * square.perimeter(3))

    def test_area_half_side(self):
        self.assertEqual(square.area(4), 4 * square.area(2))

    def test_perimeter_half_side(self):
        self.assertEqual(square.perimeter(4), 2 * square.perimeter(2))

    def test_area_float_precision(self):
        self.assertEqual(square.area(1.23456789), 1.23456789 ** 2)

    def test_perimeter_float_precision(self):
        self.assertEqual(square.perimeter(1.23456789), 4 * 1.23456789)

    def test_area_true_false(self):
        self.assertEqual(square.area(True), 1)
        self.assertEqual(square.area(False), 0)

    def test_perimeter_true_false(self):
        self.assertEqual(square.perimeter(True), 4)
        self.assertEqual(square.perimeter(False), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
