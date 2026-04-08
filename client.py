class Client:
    def __init__(self, full_name, age, contacts, client_id):
        if age < 18:
            raise ValueError("Клиент должен быть старше 18 лет.")
        self.full_name = full_name
        self.age = age
        self.contacts = contacts
        self.id = client_id
        self.status = "Active"
        self.accounts = []
        self.failed_login_attempts = 0

    def add_account(self, account):
        self.accounts.append(account)