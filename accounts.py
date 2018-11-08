class Accounts:
    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    user_accounts = []

    def save_account(self):
        '''
        this is a save function that appends the account to the user_accounts array
        '''
        Accounts.user_accounts.append(self)

    def delete_account(self):
        '''
        a function used to delete a selected account
        '''
        Accounts.user_accounts.remove(self)
    @classmethod
    def find_by_user_name(cls, user_name):
        '''
        this is a function tha checks whether the username provided by the username is available and if it is it returns the account
        '''
        for account in cls.user_accounts:
            if account.user_name == user_name:
                return account
