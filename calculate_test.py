import unittest
from calculate import Calculate

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculate()

    def test_add_method_returns_correct_result(self):
        self.assertEqual(self.calc.add(2, 2), 5)

if __name__ == '__main__':
    unittest.main()
