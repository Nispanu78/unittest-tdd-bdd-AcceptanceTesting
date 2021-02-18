import unittest

# assertDictEqual(d1, d2, msg=None)
def test_assert_dict_equal(self):
    expected = {'a': 'b', 'c': 'd'}
    actual = {'c': 'd', 'a': 'b'}
    self.assertDictEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
