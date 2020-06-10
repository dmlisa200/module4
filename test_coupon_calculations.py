import unittest
from store.coupon_calculations import calculate_price


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(calculate_price(8, 5, 10), 8.28, places=2)
        self.assertAlmostEqual(calculate_price(8, 5, 15), 7.86, places=2)
        self.assertAlmostEqual(calculate_price(8, 5, 20), 7.43, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 10), 2.98, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 15), 2.56, places=2)
        self.assertAlmostEqual(calculate_price(8, 10, 20), 2.13, places=2)


if __name__ == '__main__':
    unittest.main()
