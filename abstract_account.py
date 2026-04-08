from abc import ABC, abstractmethod
import uuid

class AbstractAccount(ABC):
    def __init__(self, owner_name, balance=0):
        self.account_id = str(uuid.uuid4())[:8]
        self.owner = owner_name
        self._balance = balance
        self.status = "active"

    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def withdraw(self, amount): pass