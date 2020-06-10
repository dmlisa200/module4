import unittest
from coupon_calculations import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(calculate_price(8, 5, 10), 8.81, places=2)
        self.assertAlmostEqual(calculate_price(8, 5, 15), 8.65, places=2)
        self.assertAlmostEqual(calculate_price(8, 5, 20), 8.49, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 10), 5.95, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 15), 5.95, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 20), 5.95, places=2)
"""
    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(calculate_price(25, 5, 10), 27.03, places=2)
        self.assertAlmostEqual(calculate_price(25, 5, 15), 25.97, places=2)
        self.assertAlmostEqual(calculate_price(25, 5, 20), 24.91, places=2)
        self.assertAlmostEqual(calculate_price(25, 10, 10), 22.26, places=2)
        self.assertAlmostEqual(calculate_price(25, 10, 15), 21.47, places=2)
        self.assertAlmostEqual(calculate_price(25, 10, 20), 20.67, places=2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(calculate_price(45, 5, 10), 50.11, places=2)
        self.assertAlmostEqual(calculate_price(45, 5, 15), 47.99, places=2)
        self.assertAlmostEqual(calculate_price(45, 5, 20), 45.87, places=2)
        self.assertAlmostEqual(calculate_price(45, 10, 10), 45.34, places=2)
        self.assertAlmostEqual(calculate_price(45, 10, 15), 43.49, places=2)
        self.assertAlmostEqual(calculate_price(45, 10, 20), 41.63, places=2)

    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(calculate_price(55, 5, 10), 47.70, places=2)
        self.assertAlmostEqual(calculate_price(55, 5, 15), 45.05, places=2)
        self.assertAlmostEqual(calculate_price(55, 5, 20), 42.40, places=2)
        self.assertAlmostEqual(calculate_price(55, 10, 10), 42.93, places=2)
        self.assertAlmostEqual(calculate_price(55, 10, 15), 40.55, places=2)
        self.assertAlmostEqual(calculate_price(55, 10, 20), 38.16, places=2)
"""

if __name__ == '__main__':
    unittest.main()
