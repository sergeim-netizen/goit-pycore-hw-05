# task2.py

import re
from typing import Callable

def generator_numbers(text: str):
    """
    Генератор, який шукає дійсні числа в тексті та повертає їх.
    """
    # Регулярний вираз для пошуку дійсних чисел (з десятковою крапкою),
    # оточених пробілами (або на початку/кінці рядка).
    # \b - "межа слова", гарантує, що число відокремлене.
    pattern = r'\b\d+\.\d+\b'
    
    # re.finditer повертає ітератор по всіх знайдених збігах
    for match in re.finditer(pattern, text):
        # yield перетворює цю функцію на генератор
        # float() перетворює знайдене значення (рядок) на число
        yield float(match.group(0))

def sum_profit(text: str, func: Callable):
    """
    Підсумовує всі числа, знайдені генератором 'func' у тексті 'text'.
    """
    total = 0
    # Ітеруємо по генератору, який повертає func(text)
    for number in func(text):
        total += number
    return total

# --- Приклад використання ---
if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")  # Очікуване виведення: 1351.46
