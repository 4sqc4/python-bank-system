from abstract_account import AbstractAccount
from exceptions import *

class BankAccount(AbstractAccount):
    def __init__(self, owner_name, balance=0, currency="RUB"):
        super().__init__(owner_name, balance)
        self.currency = currency

    def deposit(self, amount):
        if self.status != "active": raise AccountFrozenError("Счет не активен")
        if amount <= 0: raise InvalidOperationError("Сумма должна быть > 0")
        self._balance += amount

    def withdraw(self, amount):
        if self.status != "active": raise AccountFrozenError("Счет не активен")
        if amount > self._balance: raise InsufficientFundsError("Мало средств")
        self._balance -= amount

    def __str__(self):
        return f"[Счет] {self.owner} | ID: {self.account_id} | Баланс: {self._balance} {self.currency}"