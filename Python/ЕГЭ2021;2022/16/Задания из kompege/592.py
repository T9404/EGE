'''
Алгоритм вычисления функций F(n) и G(n) задан следующими соотношениями:

F(n) = G(n) = 1 при n = 1
F(n) = F(n–1) – n · G(n–1), при n > 1
G(n) = F(n–1) + 2· G(n–1), при n > 1

Чему равно значение функции G(18)?
'''
# https://prnt.sc/3NGYFFg4YxJ4


def g(n):
    if n == 1:
        return 1

    elif n > 1:
        return f(n - 1) + 2 * g(n - 1)


def f(n):
    if n == 1:
        return 1

    elif (n > 1):
        return f(n - 1) - n * g(n - 1)


print(g(18))
