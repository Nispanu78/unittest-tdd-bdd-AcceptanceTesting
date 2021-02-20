import unittest
from account import Account

class TestAccount(unittest.TestCase):
    def test_account_object_can_be_created(self):
        account = Account()

if __name__ == '__main__':
    unittest.main()
