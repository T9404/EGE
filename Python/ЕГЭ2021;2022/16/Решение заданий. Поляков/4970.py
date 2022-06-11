'''
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, 
задан следующими соотношениями:
F(0) = 8
F(n) = 5 + F(n / 3) если n > 0 и n делится на 3
F(n) = F(n // 3) в остальных случаях
Здесь // означает деление нацело. Определите количество значений n 
на отрезке [1, 100 000 000], для которых F(n) = 18.
'''
# https://prnt.sc/aUk26Bt-TwEu


# (I) Способ

from itertools import product


def system_3(number):
    number_3 = ''

    while number:
        number_3 += str(number % 3)
        number //= 3

    return int(number_3[::-1])


answer, mak = 0, system_3(100_000_000)  # по условию: на отрезке [1, 100 000 000]


for r in range(1, 18):
    for i in product('012', repeat=r):
        num = ''.join(i)

        if int(num) > mak:
            break

        if (num[0] != '0') and (num.count('0') == 2):
            answer += 1


print(answer)


'''
Как догодаться до 3ой системы счисления и 2ух нулей?

1) В алгоритме присутствует целочисленное деление на 3
2) Выведите первые числа. Что у них общего в 3 с.с?
'''





# (II) Способ


road = [0] * 100_000_000
road[0] = 8


for i in range(1, 100_000_000):
    if (i % 3 == 0):
        road[i] = 5 + road[i // 3]
    else:
        road[i] = road[i // 3]


print(road.count(18))
