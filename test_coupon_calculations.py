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


if __name__ == '__main__':
    unittest.main()
