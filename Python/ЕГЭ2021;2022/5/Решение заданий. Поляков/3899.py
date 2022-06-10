""" 
Алгоритм получает на вход натуральное число N > 1 и строит по нему новое 
число R следующим образом:
1) Строится двоичная запись числа N.
2) Подсчитывается количество нулей и единиц в полученной записи. 
Если их количество одинаково, в конец записи добавляется её последняя цифра. 
В противном случае в конец записи добавляется цифра, которая встречается реже.
3) Шаг 2 повторяется ещё два раза.
4) Результат переводится в десятичную систему счисления.
При каком наименьшем исходном числе N > 80 в результате работы алгоритма получится 
число, кратное 4?
"""
# https://prnt.sc/xjPm1I7u7brU


def f(x):
    x_2 = bin(x)[2:]

    for _ in range(3):
        if x_2.count('1') == x_2.count('0'):
            x_2 += x_2[-1]
        else:
            x_2 = (x_2 + '0') if (x_2.count('1') >
                                  x_2.count('0')) else (x_2 + '1')

    return int(x_2, 2)


for x in range(81, 100):
    if f(x) % 4 == 0:
        print(x)
        break
