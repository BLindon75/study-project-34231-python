# **Завдання 2: Створення та імпорт власних модулів**
# Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі створіть наступні функції:
# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.
def calculate_average(numbers):
    if len(numbers) != 0:
        a = 0
        for x in numbers:
            a += x
        return a / len(numbers)
    else:
        print('Your list is empty!')

def find_max(numbers):
    if len(numbers) != 0:
        return max(numbers)
    else:
        print('Your list is empty!')
