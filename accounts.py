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
