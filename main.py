from bank import Bank
from client import Client
from bank_account import BankAccount
from exceptions import InvalidOperationError

def main():
    bank = Bank()
    print("=== Консольный Банк v1.0 ===")

    # --- ЧАСТЬ 1: РЕГИСТРАЦИЯ ПОЛЬЗОВАТЕЛЕЙ ---
    entry_choice = input("Создать нового пользователя? (да/нет): ").strip().lower()
    
    if entry_choice == "да":
        while True:
            try:
                name = input("\nВведите ФИО: ")
                age = int(input("Введите возраст: "))
                contacts = input("Введите контакты: ")
                c_id = input("Придумайте ID: ")

                new_client = Client(name, age, contacts, c_id) # [cite: 90]
                bank.add_client(new_client) # 
                print(f"Система: Клиент {name} успешно добавлен.")
            except Exception as e:
                print(f"Ошибка: {e}")

            repeat = input("Добавить еще одного? (да/нет): ").strip().lower()
            if repeat != 'да':
                break

    # --- ЧАСТЬ 2: КОНТЕКСТНОЕ МЕНЮ (АНАЛОГ ТВОЕГО C# КОДА) ---
    while True:
        print("\nВыберите действие:")
        print("1. Список всех клиентов")
        print("2. Открыть счет")
        print("3. Вход в систему (Аутентификация)")
        print("4. Проверить транзакцию (Безопасность)")
        print("5. Отправить уведомление")
        print("0. Выход")
        
        choice = input("> ").strip()

        if choice == "1":
            print("\n--- СПИСОК КЛИЕНТОВ ---")
            clients = bank.get_all_clients()
            if not clients:
                print("В базе пока нет клиентов.")
            else:
                for i, c in enumerate(clients, 1):
                    print(f"{i}. {c.full_name} (ID: {c.id}) | Статус: {c.status}")

        elif choice == "2":
            target_id = input("Введите ID клиента для открытия счета: ")
            client = bank.clients.get(target_id)
            if client:
                # Создаем базовый аккаунт [cite: 119]
                new_acc = BankAccount(client.full_name) 
                client.add_account(new_acc)
                print(f"[Успех] Открыт счет {new_acc.account_id} для {client.full_name}")
            else:
                print("Ошибка: Клиент с таким ID не найден.")

        elif choice == "3":
            auth_id = input("Введите ID: ")
            password = input("Введите пароль: ")
            # Метод с защитой от 3-х попыток 
            bank.authenticate_client(auth_id, password) 

        elif choice == "4":
            try:
                amount = float(input("Введите сумму операции: "))
                # Проверка подозрительных сумм (>100k) 
                bank.check_transaction(amount) 
            except ValueError:
                print("Ошибка: введите число.")

        elif choice == "5":
            msg = input("Введите текст сообщения: ")
            # Проверка времени (запрет с 00:00 до 05:00) 
            bank.send_notification(msg) 

        elif choice == "0":
            print("Завершение работы. Прощай!")
            break
        
        else:
            print("Неверный ввод. Выберите пункт от 0 до 5.")

if __name__ == "__main__":
    main()