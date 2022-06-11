'''
Алгоритм вычисления значения функции F(n), где n – целое неотрицательное число, 
задан следующими соотношениями:
F(n) = 0 при n = 0
F(n) = F(n/2) - 1 при чётных n > 0
F(n) = 3 + F(n–1) при нечётных n > 0
Сколько различных значений может принимать функция F(n) для чисел n, меньших 1000?
'''
# https://prnt.sc/FwgvUd7OAxgK


def f(n):
    if n == 0:
        return 0
    elif (n > 0) and (n % 2 == 0):
        return f(n // 2) - 1
    elif (n > 0) and (n % 2 != 0):
        return 3 + f(n - 1)


unique = set()

for n in range(1, 1000):
    unique.add(f(n))

print(len(unique))
