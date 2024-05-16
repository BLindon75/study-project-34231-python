# **Завдання 1: Робота з функціями**
# Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:
# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a*b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        print('Sorry, you can\'t divide on 0, try again')

