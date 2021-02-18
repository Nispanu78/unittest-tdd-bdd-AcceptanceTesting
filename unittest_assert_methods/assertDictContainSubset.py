import unittest

# assertDictContainsSubset(expected, actual, msg=None)
def test_assert_dict_contains_subset(self):
    expected = {'a': 'b'}
    actual = {'a': 'b', 'c': 'd', 'e': 'f'}
    self.assertDictContainsSubset(expected, actual)

if __name__ == '__main__':
    unittest.main()
