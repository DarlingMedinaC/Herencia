class Cuenta_Bancaria:
    def __init__(self, account_number=None, owner_name=None, balance: float = 0):
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance

    def __str__(self):
        return f'Cuenta Bancaria: {self._attribute_dict().__str__()}'

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        self._owner_name = owner_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def credit(self, value: float = 0):
        self._balance = float(self._balance) + float(value)
        return self._balance

    def debit(self, value: float = 0):
        self._balance = float(self._balance) - float(value)
        return self._balance

    def show_balance(self):
        print(self._balance)
