from bank_account import BankAccount
from exceptions import InsufficientFundsError

class SavingAccount(BankAccount):
    def __init__(self, owner_name, balance, monthly_rate, min_balance=1000):
        super().__init__(owner_name, balance)
        self.monthly_rate = monthly_rate
        self.min_balance = min_balance

    def withdraw(self, amount):
        self._check_status()
        # Проверяем, останется ли на счету минимально допустимая сумма
        if self._balance - amount < self.min_balance:
            raise InsufficientFundsError(f"Нельзя снять. Минимальный остаток должен быть {self.min_balance}")
        super().withdraw(amount)

    def calculate_monthly_profit(self):
        """Расчет прибыли по процентной ставке"""
        return self._balance * (self.monthly_rate / 100)