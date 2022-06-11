'''
Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n. Так, например,

14&5 = 11102&01012 = 01002 = 4 . Определите наименьшее натуральное число A, такое что выражение

( (x & 26 ≠ 0) ∨ (x & 13 ≠ 0)) → ((x & 29 = 0) → (x & A ≠ 0))

тождественно истинно (то есть принимает значение 1 при любом натуральном значении переменной x)?
'''
# https://prnt.sc/gZRfp6p4vhsE


def f(x, a):
    return ((x & 26 != 0) or (x & 13 != 0)) <= ((x & 29 == 0) <= (x & a != 0))


for a in range(1, 10000):
    if all(f(x, a) == 1 for x in range(1, 10000)):
        print(a)
        break
