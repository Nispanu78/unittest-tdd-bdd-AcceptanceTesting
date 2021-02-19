import unittest
from calculator import Calculate

# assertAlmostEqual(x, y, places=None, msg=None, delta=None)
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        print("Hello!")
        self.assertAlmostEqual(1, 1)
        self.assertEqual(self.calc.add(2, 2), 5)

    def test_add_method_raises_typeerror_if_not_ints(self):
        self.assertRaises(TypeError, self.calc.add, "Hello", "World")



if __name__ == '__main__':
    unittest.main()
