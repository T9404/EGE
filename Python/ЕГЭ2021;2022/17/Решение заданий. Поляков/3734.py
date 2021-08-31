#Решение №1
def decto2(x):
    x2 = ''
    while x > 0:
        x2 += str(x % 2)
        x //= 2
    return x2[::-1]

def ok(n):
    return (n % 2 == 1) and\
         (decto2(n).count('0') == 5)\
         and ((n % 3 == 0) and (n % 11 == 0))

a = [n for n in range(10, 9999+1) if ok(n)]
print(len(a), a[-1])



#Решение №2

k = 0
mak = float('-inf')
def f(x):
    new_x = bin(x)[2:]
    if new_x.count('0') == 5:
        return 1
    else:
        return 0
for i in range(10, 9999+1):
    if f(i) and i % 3 == 0 and i % 11 == 0 and i % 2 == 1:
        k+=1
        mak = max(mak, i)
print(k, mak)

# Последняя цифра числа – это остаток от деления этого числа на основание системы счисления.
'''
Например, 212_{3} = 2+1*3+2*3^{2} = 23_{10}. Разделим 23 на основание системы 3,
получим 7 и 2 в остатке (2 – это последняя цифра числа в троичной системе).
Разделим 23 на 9 (основание в квадрате), получим 18 и 5 в остатке (5 = 12_{3}).
https://ege-study.ru/ru/ege/materialy/informatika/zadacha-16-razbor-razlichnyx-tipov-zadach/
'''

