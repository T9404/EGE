""""
Автомат обрабатывает натуральное число N > 1 по следующему алгоритму:
1) Строится двоичная запись числа N.
2) В конец записи (справа) дописывается вторая справа цифра двоичной записи.
3) В конец записи (справа) дописывается вторая слева цифра двоичной записи.
4) Результат переводится в десятичную систему.
Пример. Дано число N = 11. Алгоритм работает следующим образом.
1) Двоичная запись числа N: 11 = 10112
2) Вторая справа цифра 1, новая запись 101112.
3) Вторая слева цифра 0, новая запись 1011102.
4) Десятичное значение полученного числа 46.
При каком наименьшем числе N в результате работы алгоритма получится R > 170? 
В ответе запишите это число в десятичной системе счисления.
"""
# https://prnt.sc/zhhDAOhq2s_j


for N in range(2, 10000):
    new_number = bin(N)[2:]

    new_number += new_number[-2]
    new_number += new_number[1]

    if int(new_number, 2) > 170:
        print(N)
        break
