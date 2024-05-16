# **Завдання 2: Створення та імпорт власних модулів**

# Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`), який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.

# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.

import utilities

new_list = list(map(int, input('Please advise numbers: ').split()))


calculate_average = utilities.calculate_average(new_list)
find_max = utilities.find_max(new_list)

print(f'An average number  in our list: {calculate_average}')

print(f'A max number  in our list: {find_max}')
