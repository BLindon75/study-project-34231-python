# ### Списки:
# 1. **Робота із списками:**
#    Завдання: Створіть список чисел. Додайте до списку числа 10 і 20, видаліть число 10 і виведіть отриманий список.

a = [4, 5, 6, 8, 0, 11]

a.extend([10, 20])

a.remove(10)

print(a)
# 2. **Знаходження суми:**
#    Завдання: Створіть список чисел. Знайдіть та виведіть суму всіх чисел у списку.

a = [4, 7, 232, -45, 100, 32]

b = sum(a)

print(b)
# 3. **Подвійні значення:**
#    Завдання: Створіть список чисел. Подвойте кожне число у списку та виведіть результат.
a = [4, 7, 232, -45, 100, 32]

b = []

for x in a:

    b.append(x*2)

print(b)
# ### Кортежі:
# 1. **Робота із кортежами:**
#    Завдання: Створіть кортеж з трьох різних предметів, таких як ("яблуко", "банан", "апельсин"). Виведіть кожен елемент кортежу окремо.

tuple_1 = ('apple', 'banana', 'orange')

print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[-1])
# 2. **Об'єднання кортежів:**
#    Завдання: Створіть два кортежі з числами і об'єднайте їх у новий кортеж. Виведіть отриманий кортеж.

tuple_1 = (1, 5, 6, 7, 78)

tuple_2 = (4, 4, 3, 56, 5)

print(tuple_1 + tuple_2)
# ### Словники:
# 1. **Робота із словниками:**
#    Завдання: Створіть словник, що містить інформацію про вашого улюбленого спортсмена (ім'я, вік, спорт, команда тощо). Виведіть цю інформацію на екран.

sportsman = {
    'name': 'Muhammad Ali',
    'age': 'immortal',
    'sport': 'box',
    'team': 'alone',
    'gender': 'man'
}

print(f'I am gonna to introduce my favorite sportsman')

print('----------------------------------------------')

print('His name is', sportsman['name'])
print('His age is uncounted, because He is', sportsman['age'])
print('He used to', sportsman['sport'])
print('He did it', sportsman['team'])
print('He is real', sportsman['gender'])

# 2. **Оновлення словника:**
#    Завдання: Створіть словник, що містить ваші улюблені книги (назва книги та рік видання). Додайте до словника нову улюблену книгу та виведіть оновлений словник.

my_favorite_books = {
    'The Lord of the Rings': '1954',
    'Nineteen Eighty-Four': '1949',
    'To Kill a Mockingbird': '1960',
    'The Catcher in the Rye': '1951'
}

my_favorite_books['Of Human Bondage'] = '1915'

for books, years in my_favorite_books.items():
    print(f'A Book \'{books}\' was published in {years}')
# 3. **Пошук значення:**
#    Завдання: Створіть словник, що містить інформацію про країни та їх столиці. Запитайте користувача про назву країни і виведіть столицю цієї країни (якщо така країна є у словнику).
# Завершіть кожне завдання, використовуючи вбудовані методи для списків, кортежів та словників. Бажаю успіхів у виконанні цих завдань!

countries = {
    'Ukraine': 'Kyiv',

    'Poland': 'Warsaw',

    'Greece': 'Athens',

    'Italy': 'Rome',

    'Germany': 'Berlin'
}

while countries:
    country = input('Please advise a name of a country: ')

    if country in countries:
        capital = countries.pop(country)
        print(f'You found out that {capital} is the capital of {country}')
    else:
        print('Sorry, try again')

print('We found all capitals')