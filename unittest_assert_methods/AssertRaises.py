import unittest

# assertRaises(exception, method, arguments, msg=None)
def test_assert_raises(self):
    self.assertRaises(ValueError, int, "a")

def test_assert_raises_alternative(self):
    with self.assertRaises(AttributeError):
        [].get

if __name__ == '__main__':
    unittest.main()
