# **Завдання 1: Наслідування**
# Створіть базовий клас `Vehicle` (транспортний засіб), який містить наступні атрибути:
# - `make` (виробник)
# - `model` (модель)
# - `year` (рік виробництва)
# Додайте конструктор класу `Vehicle`, який ініціалізує ці атрибути.
# Створіть підкласи (похідні класи) від `Vehicle` для різних видів транспорту, наприклад, `Car`, `Motorcycle`, `Bicycle`, тощо.
# Кожен підклас повинен мати додаткові атрибути та методи, які є специфічними для цього виду транспорту.
# Наприклад, для класу `Car` можна додати атрибут `fuel_type` та метод `start_engine()`.
# Створіть об'єкти для кожного з підкласів та виведіть їхні атрибути на екран.

class Vehicle:
    '''It is a base class'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_attr(self):
        print(self.__dict__)

class Car(Vehicle):
    '''It is a child's class'''

    def __init__(self, make, model, year, number_of_passengers):
        super().__init__(make, model, year)
        self.number_of_passengers = number_of_passengers

    def start_engine(self):
        print('Engine started')

class Bicycle(Vehicle):
    '''It is a child's class'''
    def __init__(self, make, model, year, number_of_wheels):
        super().__init__(make, model, year)
        self.number_of_wheels = number_of_wheels

    def light(self):
        print('The front/back lights are on')

class Plane(Vehicle):
    '''It is a child's class'''
    def __init__(self, make, model, year, number_of_engines):
        super().__init__(make, model, year)
        self.number_of_engines = number_of_engines

    def crew(self):
        print(f'You are welcome, today, on our deck, a team works from {self.make}!')

car_1 = Car("BMW", 'X5', 2019, 6)
car_1.get_attr()
car_1.start_engine()

bicycle_1 = Bicycle("Ukraina", '14', 1965, 2)
bicycle_1.get_attr()
bicycle_1.light()

plane_1 = Plane("Airbus", '5353', 1999, 4)
plane_1.get_attr()
plane_1.crew()


## **Завдання 2: Поліморфізм**
# Створіть метод `display_info()` у базовому класі `Vehicle`, який виводить загальну інформацію про транспортний засіб
# (наприклад, "Це [виробник] [модель] [рік] року виробництва.").
# В кожному з підкласів перевизначте метод `display_info()` для виведення специфічної інформації про цей вид транспорту.
# Створіть список об'єктів з різних видів транспорту, викличте метод `display_info()` для кожного об'єкта,
# і спостерігайте за тим, як поліморфізм дозволяє викликати правильну версію методу для кожного об'єкта.
class Vehicle:
    '''It is a base class'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_attr(self):
        print(self.__dict__)

    def display_info(self):
        print(f'This is a {self.make} {self.model} made in {self.year}.')

class Car(Vehicle):
    '''It is a child's class'''

    def __init__(self, make, model, year, number_of_passengers):
        super().__init__(make, model, year)
        self.number_of_passengers = number_of_passengers

    def start_engine(self):
        print('Engine started')

    def display_info(self):
        print(f'This is a car: {self.make} {self.model} made in {self.year}. It can carry {self.number_of_passengers} passengers.')

class Bicycle(Vehicle):
    def __init__(self, make, model, year, number_of_wheels):
        super().__init__(make, model, year)
        self.number_of_wheels = number_of_wheels

    def light(self):
        print('The front/back lights are on')

    def display_info(self):
        print(f'This is a bicycle: {self.make} {self.model} made in {self.year}. It has {self.number_of_wheels} wheels.')

class Plane(Vehicle):
    def __init__(self, make, model, year, number_of_engines):
        super().__init__(make, model, year)
        self.number_of_engines = number_of_engines

    def crew(self):
        print(f'You are welcome, today, on our deck, a team works from {self.make}!')

    def display_info(self):
        print(f'This is a plane: {self.make} {self.model} made in {self.year}. It has {self.number_of_engines} engines.')


car_1 = Car("BMW", 'X5', 2019, 6)
bicycle_1 = Bicycle("Ukraina", '14', 1965, 2)
plane_1 = Plane("Airbus", 'A320', 1999, 2)

vehicles = [car_1, bicycle_1, plane_1]

for vehicle in vehicles:
    vehicle.display_info()