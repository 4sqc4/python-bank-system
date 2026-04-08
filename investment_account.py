from bank_account import BankAccount

class InvestmentAccount(BankAccount):
    def __init__(self, owner_name, balance):
        super().__init__(owner_name, balance)
        self.assets = [] # Список словарей {'name': ..., 'value': ..., 'yield': ...}

    def add_asset(self, name, value, annual_yield):
        self.assets.append({'name': name, 'value': value, 'yield': annual_yield})

    def project_yearly_growth(self):
        """Считает общую доходность всех активов за год"""
        total_growth = 0
        for asset in self.assets:
            total_growth += asset['value'] * (asset['yield'] / 100)
        return total_growth