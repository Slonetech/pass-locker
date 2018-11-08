from accounts import Accounts
import unittest

class TestAccount(unittest.TestCase):
    def tearDown(self):
        Accounts.user_accounts = []
