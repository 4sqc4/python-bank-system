from datetime import datetime

class Bank:
    def __init__(self):
        # Используем словарь, где ключ - ID, значение - объект клиента
        self.clients = {} 

    def add_client(self, client):
        self.clients[client.id] = client

    # ВОТ ЭТОТ МЕТОД ТЕБЕ НУЖНО ДОБАВИТЬ:
    def get_all_clients(self):
        return list(self.clients.values())

    def authenticate_client(self, client_id, password):
        client = self.clients.get(client_id)
        if not client:
            print("Клиент не найден.")
            return
        # ... тут твоя логика пароля и блокировки ...
        if password == "1234":
            print(f"Добро пожаловать, {client.full_name}!")
        else:
            print("Неверный пароль.")

    def check_transaction(self, amount):
        if amount > 100000:
            print("[ALARM] Подозрительная сумма!")
        else:
            print("[OK] Операция разрешена.")

    def send_notification(self, msg):
        hour = datetime.now().hour
        if 0 <= hour < 5:
            print("[Тихий режим] Сообщение сохранено.")
        else:
            print(f"[SMS] {msg}")