# __________________________________________________________________________________
# Предусловие.
# Задачи 3 и 4 выполнить в 2-х вариантах:
# 1) В процедурном виде (весь код в одной процедуре).
# 2) В виде функций - код разбит на функции. Отдельные функции можно вынести в другие .py файлы и вызывать
# их в main.py предвварительно импортируя в main.py.


# Задача №1
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "конвертированная сумма в USD = int"
#     3. Валюту пользователя определите сами.

cash = int(input())
USD = (2.5)
exchange = (cash / USD)
print("You entered", cash, "BYN")
print("Converted amount in USD", exchange)

# Задача №2
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
#     1. На вход обменнику вводишь количество денег int.
#     2. На выходе в консоль выводится отввет в таком виде:
#                 "Ты ввёл int (Валюта)"
#                 "Конвертированная сумма в USD = int"
#                 "Конвертированная сумма в EUR = int"
#                 "Конвертированная сумма в CHF = int"
#                 "Конвертированная сумма в GBP = int"
#                 "Конвертированная сумма в CNY = int"
#     3. Валюту пользователя определите сами.

cash = int(input())
print("You entered",cash, "BYN")

USD = float(2.5)
EUR = (3.3)
CHF = (1.7)
GBP = (1.9)
CNY = (1.2)

exchange = ([cash // USD] , [cash // EUR], [cash // CHF], [cash // GBP], [cash // CNY])

print("Converted amount in USD", exchange[0])
print("Converted amount in EUR", exchange[1])
print("Converted amount in CHF", exchange[2])
print("Converted amount in GBP", exchange[3])
print("Converted amount in CNY", exchange[4])


# Задача №3
# Обменник. Создать скрипт который будет запускаться из консоли 1 раз из консоли, выдавать результат и зарываться.
# 1. На вход обменнику вводишь количество денег int.
# 2. На выходе в консоль выводится отввет в таком виде:
# "Ты ввёл int (Валюта)"
# "конвертированная сумма в USD = int"
# "конвертированная сумма в EUR = int"
# "конвертированная сумма в CHF = int"
# "конвертированная сумма в GBP = int"
# "конвертированная сумма в CNY = int"
# 3. Скипт должен выдать сообщение
# "Введите положительное число." Если число меньше 0.
# "Вы ввели не число. Введите число." Если введены буквы.
# "Вы ввели пустое поле. Введите число." Если введено пустое значение.
# 4. Валюту пользователя определите сами.

cash = int(input())
print("You entered",cash, "BYN")

USD = (2.5)
EUR = (3.3)
CHF = (1.7)
GBP = (1.9)
CNY = (1.2)

exchange = ([cash // USD] , [cash // EUR], [cash // CHF], [cash // GBP], [cash // CNY])

print("Converted amount in USD", exchange[0])
print("Converted amount in EUR", exchange[1])
print("Converted amount in CHF", exchange[2])
print("Converted amount in GBP", exchange[3])
print("Converted amount in CNY", exchange[4])

while True:

    cash = input("You entered cash BYN ")
    try:
        cash_int = int(cash)

    except ValueError:
        if not cash:
            print('You inserted empty field. Please insert a number')
            continue
        else:
            print('You inserted not a number. Please insert a number')
            continue
    if int(cash) < 0:
        print('Please insert positive amount')
        continue

    cash_int_2 = int(cash)
    print('You typed ', cash_int_2, 'BYN ')

    exchange = ([cash_int_2 // USD], [cash_int_2 // EUR], [cash_int_2 // CHF], [cash_int_2 // GBP], [cash_int_2 // CNY])

    print("Converted amount in USD", exchange[0])
    print("Converted amount in EUR", exchange[1])
    print("Converted amount in CHF", exchange[2])
    print("Converted amount in GBP", exchange[3])
    print("Converted amount in CNY", exchange[4])
    input('Press ENTER to exit')
    break


