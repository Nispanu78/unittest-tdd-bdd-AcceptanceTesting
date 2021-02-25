from lettuce import *
from account import Account
from bank import Bank

@step(u'account number 1 is a valid account')
def given_account_number_1_is_a_valid_account(step):
    account = Account(1, 50)
    bank = Bank()
    bank.add_account(account)
