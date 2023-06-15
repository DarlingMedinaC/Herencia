from cuenta import Cuenta_Bancaria

class Cuenta_ahorro(Cuenta_Bancaria):
    def __init__(self, interest: float = 0, account_number=None, owner_name=None, balance: float = 0):
        self._interest = interest
        super(Cuenta_ahorro, self).__init__(account_number=account_number, owner_name=owner_name, balance=balance)

    @property
    def interest(self):
        return self._interest

    @interest.setter
    def interest(self, interest):
        self._interest = interest

    def pay_interest(self):
        self._balance = self._balance + ((float(self._balance) * int(self._interest))/100)
        return self._balance

if __name__ == '__main__':
    Cuentas_ahorros = Cuenta_ahorro(6, '0952221842', 'darling', 320)

    Cuentas_ahorros.show_balance()
    Cuentas_ahorros.credit(1400)

    Cuentas_ahorros.show_balance()
    Cuentas_ahorros.debit(30)

    print(Cuentas_ahorros)
