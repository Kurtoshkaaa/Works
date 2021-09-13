# __________________________________________________________________________________
# #Homework PYTHON_1
a = str("text.txt")
print(a, type(a))


b = int(3)
print(b, type(b))


c = float(3.14)
print(c, type(c))


d = bytes(1)
print(d, type(d))


e = ['1', '2', '3', '4', '5', '6']
print(e, type(e))


name = "Aliaksey"
age = 28
location = "Minsk"
f = (name, age, location)
print(f, type(f))


friends = {"Lesha", "Sasha", "Vika", "Lesha"}
g = set(friends)
print(g, type(g))


# one = set([1, 2, 3])
two = frozenset([4, 5, 6, 7])
# three = set({58, 49, 310, 211, 112, two})
print(two, type(two))


i = {"A": 1, "B": 2, "C": 3}
# print (list (i))
# print (list(i.values()))
print(i, type(i))


# __________________________________________________________________________________

#Вывел в консоль и определил тип переменной.

# D:\LESHA\COURSES\PYTHON_PROJECT\venv\Scripts\python.exe D:/LESHA/COURSES/PYTHON_PROJECT/main.py
# text.txt <class 'str'>
# 3 <class 'int'>
# 3.14 <class 'float'>
# b'\x00' <class 'bytes'>
# ['1', '2', '3', '4', '5', '6'] <class 'list'>
# ('Aliaksey', 28, 'Minsk') <class 'tuple'>
# {'Vika', 'Sasha', 'Lesha'} <class 'set'>
# frozenset({4, 5, 6, 7}) <class 'frozenset'>
# {'A': 1, 'B': 2, 'C': 3} <class 'dict'>
#
# Process finished with exit code 0
# __________________________________________________________________________________
#Создать 2 переменные "String" . Cоздать переменную в которой суммируете эти переменные. Вывести в консоль.

life_1 = ("I love")
life_2 = ("life")
Conclusion = (life_1 + " " + life_2)
print(Conclusion)


# __________________________________________________________________________________
#Создать 2 переменные "Integer" . Cоздать переменную в которой суммируете эти переменные. Вывести в консоль.

entire_1 = int(3)
entire_2 = int(5)
amount = (entire_1 + entire_2)
print(amount)


# __________________________________________________________________________________
#Создать 2 переменные "Integer" . Cоздать переменную в которой нужно будет разделить эти переменные. Вывести в консоль.

mount_1 = int(10)
mount_2 = int(5)
wasteland = (mount_1 // mount_2)
print(wasteland)


# __________________________________________________________________________________
#Создать 2 переменные "Integer" . Cоздать переменную в которой нужно будет умножить эти переменные. Вывести в консоль.

rain_1 = int(3)
rain_2 = int(3)
weather = (rain_1 * rain_2)
print(weather)

# __________________________________________________________________________________
#Создайте переменную в которой разделите без остатка переменные Int. Вывести в консоль.

ball_1 = int(30)
ball_2 = int(7)
basket = (ball_1 // ball_2)
print(basket)

# __________________________________________________________________________________
#Создайте переменную в которой разделите c остатком переменные Int. Вывести в консоль.

day_1 = int(30)
day_2 = int(7)
week = (day_1 / day_2)
print(week)
#_______________________________________________________________________________________








