import unittest

def test_assert_almost_equal_delta_0_5(self):
    self.assertAlmostEqual(1, 1.2, delta=0.5)

def test_assert_almost_equal_places(self):
    self.assertAlmostEqual(1, 1.00001, places=4)

if __name__ == '__main__':
    unittest.main()
