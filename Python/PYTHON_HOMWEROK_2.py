# Python.Homework_  # 2
#
# 1) Создать 2 переменных типа String с разными значениями
first = "mercedes"
second = "audi"

# 2) Создать 4 переменных типа Integer с разными значениями
a, b, c, d = 2, 5, 7, 8

# 3) Создать 3 переменных типа Float с разными значениями
fl1, fl2, fl3 = 1.5, 2.4, 3.5

# 4) Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
print(a > b)
print(a < b)
print(c >= d)
print(a == d)
print((c + d) >= a)
print(a != c)
print(c == b)
print(d < (a + b))
print(a * d > c * b)
print(d != (a - b))
print(a > d * (-1))
print(b <= d)
print(c * d != (a + b))
print((d + 4) < c)
print(c != b)

# 5) Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты вывести в консоль.
print(fl1 > fl2)
print(fl1 < fl3)
print(fl3 >= fl2)
print(fl1 == fl3)
print((fl1 + fl2) >= fl3)
print(fl1 != fl2)
print(fl1 == fl2)
print(fl2 < (fl1 + fl3))
print(fl3 > fl1 * fl2)

# 6) Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями
# (end, or, not).Pезультаты вывести в консоль.
print(a > b and b < c)
print(a < b or c < d)
print(not c >= d)
print(a == d or d != b)
print(not (c + d) >= a)
print(not a != c)
print(c == b and a > d)
print(not d < (a + b))
print(a * d > c * b or a < b)
print(not d != (a - b))


# 7) Сделать скрипт используя функцию input().
# 1. Функция должна на вход принимать целое число.
# 2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
#
while True:
    print("Введите целое число")
    x = int(input())
    if x > 30:
        print("Вы ввели число = " + str(x) + ", которое больше 30")
    elif x == 30:
        print("Вы ввели число = " + str(x) + ", которое равно 30")
    else:
        print("Вы ввели число = " + str(x) + ", которое меньше 30")


# 8) Сделать скрипт используя функцию input().
# 1. Функция должна на вход принимать целое число.
# 2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
# 3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"


import random
while True:
    print("Введите целое число")
    x = int(input())
    rnd = random.randrange(1, 100)
    print("сгенерированное число = " + str(rnd))
    if x > rnd:
        print("Вы ввели число = " + str(x) + ", которое больше сгенерированного числа")
    elif x == rnd:
        print("Вы ввели число = " + str(x) + ", которое равно сгенерированному числу")
    else:
        print("Вы ввели число = " + str(x) + ", которое меньше сгенерированного числа")

# 9) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомных 2 целых числа (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
# В заданиях # 7, 8, 9, сами выберите какие условные операторы и сравнения использовать.

import random
while True:
    print("Введите целое число")
    x = int(input())
    rnd1 = random.randrange(1, 100)
    rnd2 = random.randrange(1, 100)
    print("первое сгенерированное число = " + str(rnd1))
    print("второе сгенерированное число = " + str(rnd2))
    if x > rnd1:
        if x > rnd2:
            print("Вы ввели число = " + str(x) + ", которое больше 1 и 2 сгенерированного числа")
        elif x == rnd2:
            print("Вы ввели число = " + str(x) + ", которое больше 1-го и равно 2 сгенерированному числу")
        else:
            print("Вы ввели число = " + str(x) + ", которое больше 1 и меньше 2 сгенерированного числа")
    elif x == rnd1:
        if x > rnd2:
            print("Вы ввели число = " + str(x) + ", которое равно 1 и больше 2 сгенерированного числа")
        elif x == rnd2:
            print("Вы ввели число = " + str(x) + ", которое равно 1 и 2 сгенерированному числу")
        else:
            print("Вы ввели число = " + str(x) + ", которое равно 1 и меньше 2 сгенерированного числа")
    else:
        if x > rnd2:
            print("Вы ввели число = " + str(x) + ", которое меньше 1 и больше 2 сгенерированного числа")
        elif x == rnd2:
            print("Вы ввели число = " + str(x) + ", которое меньше 1 и равно 2 сгенерированному числу")
        else:
            print("Вы ввели число 5"

            "= " + str(x) + ", которое меньше 1 и 2 сгенерированного числа")
            "= " + str(x) + ", которое меньше 1 и 2 сгенерированного числа")
