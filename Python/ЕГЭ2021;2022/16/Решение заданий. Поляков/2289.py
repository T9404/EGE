'''
Алгоритм вычисления значения функции F(n), где n – натуральное число, 
задан следующими соотношениями:
F(n) = n*n + 11, при n ≤ 15
F(n) = F(n//2) + n*n*n - 5*n, при чётных n > 15
F(n) = F(n-1) + 2*n + 3, при нечётных n > 15
Здесь // обозначает деление нацело. Определите количество натуральных 
значений n из отрезка [1; 1000], для которых значение F(n) содержит не менее трёх цифр 6.
'''
# https://prnt.sc/9RZubH7JD8se


def func(n):
    if n <= 15:
        return n * n + 11
    elif n > 15 and n % 2 == 0:
        return func(n // 2) + n ** 3 - 5 * n
    elif n > 15 and n % 2 != 0:
        return func(n - 1) + 2 * n + 3


count = 0


for x in range(1, 1000+1):
    number = func(x)
    if str(number).count('6') >= 3:
        count += 1


print(count)
