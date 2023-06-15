from cuenta import Cuenta_Bancaria

class Cuenta_corriente(Cuenta_Bancaria):
    def __init__(self, account_number=None, owner_name=None, balance: float = 0, has_check=bool):
        self._has_check = has_check
        super(Cuenta_corriente, self).__init__(account_number=account_number, owner_name=owner_name, balance=balance)

    @property
    def has_check(self):
        return self._has_check

    @has_check.setter
    def has_check(self, has_check):
        self._has_check = has_check

    def pay_check(self):
        self._balance = self._balance - float(self._balance)
        return self._balance

if __name__ == '__main__':
    Cuentas_corrientes = Cuenta_corriente('0922117842', 'darling', 250, True)

    Cuentas_corrientes.show_balance()
    Cuentas_corrientes.credit(1400)

    Cuentas_corrientes.show_balance()
    Cuentas_corrientes.debit(30)

    print(Cuentas_corrientes)
