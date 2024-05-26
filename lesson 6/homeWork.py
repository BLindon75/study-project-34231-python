# **Завдання 1: Створення класу і об'єктів**
# Створіть клас `Animal`, який представляє тварину. Кожний об'єкт класу `Animal` повинен мати наступні атрибути:
# - `name` (ім'я тварини)
# - `species` (вид тварини)
# - `age` (вік тварини)

# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `make_sound()`, який буде виводити звук, який виділяє тварина.

# Створіть два об'єкта класу `Animal` з різними характеристиками та викличте їхні методи `make_sound()`.

class Animal:
    """This class represents an animal"""
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self, sound):
        print(f"{self.name} says {sound}")

animal1 = Animal('Bobik', 'dog', 3)

animal2 = Animal('Murzik','cat', 4)

animal1.make_sound('gau')
print('------------------------------')
animal2.make_sound('mow')
# **Завдання 2: Робота з об'єктами**
# Створіть клас `Rectangle`, який представляє прямокутник. Кожен об'єкт класу `Rectangle` повинен мати наступні атрибути:
# - `width` (ширина прямокутника)
# - `height` (висота прямокутника)
# Створіть конструктор класу, який ініціалізує ці атрибути при створенні об'єкта. Напишіть метод `calculate_area()`, який розраховує площу прямокутника (площа = ширина * висота).
# Створіть два об'єкта класу `Rectangle` з різними розмірами та викличте їхні методи `calculate_area()`, виведіть площу прямокутників на екран.
class Rectangle:
    """This class represents a rectangle"""
    def __init__(self, name, width, height):
        self.name = name
        self.width = width
        self.height = height
    def calculate_area(self):
            if self.height <= 0 or self.width <= 0:
             print('Coordinates can\'t be less or equal 0!!!!')
             print(f'I can\'t calculate Area of Rectangle {self.name}')
            else:
             area = self.width * self.height
             print(f'Area of Rectangle {self.name} is {area}')

Rectangle1 = Rectangle('ABCD', 3, 4)
Rectangle2 = Rectangle('QWER', 5, 0)
Rectangle1.calculate_area()
print('------------------------------')
Rectangle2.calculate_area()