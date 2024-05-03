# 1. Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None

int_1 = 4

float_1 = 4.7

str_1 = "Hello, World!"

bool_1 = True

bool_2 = False

None_1 = None

list_1 = [1, 3, 5, 43434, 4343, 0, -3]

tuple_1 = (1, 3, 5, 5, 'banana')

dict_1 = {'name': 'Alex', 'age': '25', 'height': '1,75'}

set_1 = {1, 4, 5, 7, 'Banana'}

# 2. Використати вивчені оператори та порівняти між собою числа, рядки, булеві значення, списки, словники і кортежі

print(int_1 < float_1)

print(not int_1 == float_1)

print(int_1 in set_1)

print(bool_1 == None_1 or 'o' in str_1)

print(list_1[3] > list_1[4])

print(list_1[-2] != bool_1)

print(len(set_1) == len(tuple_1) and None_1 != bool_1)

# 3. Використати вивчені функції Python:
# Робота з рядками:
#  1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()

num_str = 125

num_str_upd = str(num_str)

print(num_str_upd)

#  2. Cтворити зміну message = 'Hi, my name is Python!' За допомогою функції replace() замінити
# усі букви 'y' на '0' та 'i' на '1'.

message = 'Hi, my name is Python!'

message_1 = message.replace('y', '0')

message_2 = message_1.replace('i', '1')

print(message_2)

#  3. Cтворити зміну split_test = 'This is a split test' і розділити її по пробілах за
# допомогою функції split(), а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join

split_test = 'This is a split test'

split_test = split_test.split()

print(split_test)

string_join = " ".join(split_test)

print(string_join)

# 4. Визначити довжину рядку string_join за допомогою функції len()

print(len(string_join))

# Робота зі списками:
#  1. Cтворити змінну list_append = [1, 2, 3] і за допомогою функції append() додати туди спочатку 4, а потім 5

list_append = [1, 2, 3]

list_append.append(4)

list_append.append(5)

print(list_append)

# 2. Cтворити змінну list_extend = [4, 5, 6] і розширити цей список іншим списком[7, 8, 9] за допомогою функції extend()

list_extend = [4, 5, 6]

list_extend.extend([7, 8, 9])

print(list_extend)

# 3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()

print(list_extend.index(6))

# 4. Визначити довжину списку list_append за допомогою функції len()

print(len(list_append))

# Робота зі словниками:
#  1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} та вивести на екран дані, які знаходяться в ключах car та where

dict_test = {
    'car': 'Toyota',
    'price': 4900,
    'where': 'EU'
}

print(dict_test['car'], dict_test['where'])

#  2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення

print(dict_test.keys())

print(dict_test.values())

#  3. За допомогою функції items() вивести на екран пари ключ - значення

print(dict_test.items())