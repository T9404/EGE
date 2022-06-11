'''
Алгоритм вычисления значения функции F(n), где n – натуральное 
число, задан следующими соотношениями:
F(n) = n*n + 4*n + 3, при n > 25
F(n) = F(n+1) + 2*F(n+4), при n ≤ 25, кратных 3
F(n) = F(n+2) + 3*F(n+5), при n ≤ 25, не кратных 3
Определите количество натуральных значений n из отрезка [1; 1000], 
для которых сумма цифр значения F(n) равна 24.
'''
# https://prnt.sc/jK4bMw-IFT5V


def F(n):
    if (n > 25):
        return n * n + 4 * n + 3
    if (n <= 25) and (n % 3 == 0):
        return F(n + 1) + 2 * F(n + 4)
    if (n <= 25) and (n % 3 != 0):
        return F(n + 2) + 3 * F(n + 5)


count = 0


for a in range(1, 1001):
    value = F(a)
    summ = 0

    while value:
        summ += (value % 10)
        value //= 10
        
    if (summ == 24):
        count += 1


print(count)
