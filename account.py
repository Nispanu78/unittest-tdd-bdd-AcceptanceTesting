class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_account(self, id_num):
        return self.di.get(id_num)

class ConnectionError(Exception):
    pass
    def get_account(self, id_num):
        try:
            result = self.di.get(id_num)
        except ConnectionError:
            result = "Connection error occurred. Try Again."
        return result
