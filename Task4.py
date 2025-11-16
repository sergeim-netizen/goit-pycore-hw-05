# task4.py

def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    
    Обробляє KeyError, ValueError, IndexError, що виникають 
    у функціях-обробниках команд.
    """
    def inner(*args, **kwargs):
        try:
            # Спробуємо виконати оригінальну функцію
            return func(*args, **kwargs)
        
        except ValueError:
            # Виникає, якщо 'add' або 'change' отримали не 2 аргументи
            return "Give me name and phone please."
        
        except KeyError:
            # Виникає, якщо 'phone' або 'change' не знайшли ім'я у контактах
            return "Contact not found."
        
        except IndexError:
            # Виникає, якщо 'phone' викликане без аргументів
            return "Enter user name."

    return inner

#
# ▼▼▼ ЦЕ КЛЮЧОВА ФУНКЦІЯ, ЯКА ВСЕ ВИПРАВЛЯЄ ▼▼▼
#
def parse_input(user_input):
    """
    Розбирає введений рядок на команду та аргументи.
    """
    # 'cmd, *args' означає:
    # 1. 'cmd' - це перше слово
    # 2. 'args' - це СПИСОК з УСІХ ІНШИХ слів (може бути порожнім)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    
    # Завжди повертає 2 значення: рядок 'cmd' та список 'args'
    return cmd, args
#
# ▲▲▲ ЦЕ КЛЮЧОВА ФУНКЦІЯ, ЯКА ВСЕ ВИПРАВЛЯЄ ▲▲▲
#

@input_error
def add_contact(args, contacts):
    """
    Додає контакт.
    """
    # Ця стрічка викличе ValueError, якщо 'args' має не 2 елементи
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """
    Змінює контакт.
    """
    name, phone = args  # Може викликати ValueError
    if name not in contacts:
        raise KeyError  # Викликаємо помилку, яку зловить декоратор
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """
    Показує телефон.
    """
    name = args[0]      # Може викликати IndexError
    return contacts[name] # Може викликати KeyError

def show_all(contacts):
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts found."
    
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

#
# ▼▼▼ ЦЯ ФУНКЦІЯ ТАКОЖ ВИПРАВЛЕНА ▼▼▼
#
def main():
    """
    Головний цикл бота.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        
        # ЦЯ ПЕРЕВІРКА ВАЖЛИВА:
        # Запобігає збою, якщо користувач просто натиснув Enter
        if not user_input: 
            continue
            
        # Цей рядок тепер ЗАВЖДИ буде працювати
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
            
        elif command == "hello":
            print("How can I help you?")
            
        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))
            
        elif command == "phone":
            print(show_phone(args, contacts))
            
        elif command == "all":
            print(show_all(contacts))
            
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
