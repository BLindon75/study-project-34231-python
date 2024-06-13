# Завдання 1: Інкапсуляція
# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):
# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)
# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери).
# Потім створіть об'єкт класу "Користувач" і встановіть значення полів, а також виведіть їх на екран.

class User:
    def __init__(self, name, email, password) -> None:
        self.__name = name
        self.__email = email
        self.__password = password

    def get_atter(self):
        return self.__dict__

    def set_atter(self, attr, value):
        if type(attr) == str:
            self.__dict__[attr] = value
            return {attr: self.__dict__[attr]}
        else:
            return 'Attribute must be string'

user1 = User('admin', 'abobus.1212@gmail.vk', 'qwerty123@')
print(user1.get_atter())
print(user1.set_atter('new_password', 'QWERTY123@'))

# Завдання 2: Абстракція
# Створіть клас "Фігура" (Shape), який буде абстрактним класом. У цьому класі визначіть абстрактний метод "обчислити_площу" (calculate_area).
# Створіть підкласи цього класу для різних геометричних фігур, наприклад, "Коло" (Circle), "Прямокутник" (Rectangle) і "Трикутник" (Triangle).
# У кожному з підкласів реалізуйте метод "обчислити_площу" відповідно до формули для обчислення площі кожної фігури.
# Створіть об'єкти кожного з підкласів і використайте метод "обчислити_площу", щоб вивести площу кожної фігури на екран.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return (self.radius ** 2) * 3.14


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return (self.base * self.height) / 2


circle_1 = Circle(45)
rectangle_1 = Rectangle(45, 56)
triangle_1 = Triangle(3, 5)

print("Площа кола:", circle_1.calculate_area())
print("Площа прямокутника:", rectangle_1.calculate_area())
print("Площа трикутника:", triangle_1.calculate_area())

# Завдання 3: Користування інкапсуляцією та абстракцією у реальному коді
# Розгляньте фрагмент коду з існуючого проекту або бібліотеки та ідентифікуйте в ньому використання інкапсуляції та абстракції.
# Поясніть, як вони застосовуються і як це допомагає поліпшити читабельність та підтримку коду.

# Інкапсуляція
# Інкапсуляція означає обмеження доступу до деяких компонентів об'єкта, щоб запобігти прямій зміні стану об'єкта ззовні.
# Це робиться для забезпечення контрольованого доступу до даних.
# Наприклад, у класі User ми використовуємо інкапсуляцію для приховування полів __name, __email, __password.
# Це забезпечує безпеку даних, дозволяючи доступ до них тільки через геттери і сеттери.


# Абстракція
# Абстракція полягає в тому, щоб виділяти важливі аспекти реального об'єкта і приховувати менш важливі деталі.
# Це дозволяє зосередитися на суттєвих характеристиках об'єкта, спрощуючи розуміння та використання коду.