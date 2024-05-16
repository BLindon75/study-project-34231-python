# **Завдання 1: Робота з функціями**
# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень. Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.

import calculator

a, b = map(int, input('Please, fill down two numbers through space: ').split())
add = calculator.add(a,b)
subtract = calculator.subtract(a,b)
multiply = calculator.multiply(a,b)
divide = calculator.divide(a,b)

print(f'if you add {a} and {b}, you receive a result: {add}')
print((f'if you subtract {a} and {b}, you receive a result: {subtract}'))
print((f'if you multiply {a} and {b}, you receive a result: {multiply}'))
print((f'if you divide {a} and {b}, you receive a result: {divide}'))


