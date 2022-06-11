'''
Что нужно знать?
and ----> ∧
or  ----> v
→   ----> <=  P.S. подумайте почему
=   ----> ==
≠   ----> !=
'''





print('>>>>>')
# К.Ю.Поляков 3602
'''
Для какого наименьшего целого неотрицательного числа А выражение

(x – 2y < 3A) ∨ (2y > x) ∨ (3x > 50)
тождественно истинно, т.е. принимает значение 1 при любых целых
положительных x и y? 
'''


def f(x, y, a):
    return ((x - 2 * y) < 3 * a) or (2 * y > x) or (3 * x > 50)


for a in range(1, 100):
    good = True

    for x in range(1, 1000):
        for y in range(1, 1000):
            if not f(x, y, a):
                good = False
                break

        if not good:
            break

    if good:
        print(a)
        break








print('>>>>>>>')
# К.Ю.Поляков 3484
''' Для какого наибольшего целого неотрицательного числа А выражение

(x2 – 11x + 28 > 0) ∨ (y2 – 9y + 14 > 0) ∨ (x2 + y2 > A)
тождественно истинно, т.е. принимает значение 1 при любых целых
положительных x и y? '''

from itertools import product


for A in range(10000, 0, -1):
    cool = True

    for x, y in product(range(1000), range(1000)):
        if not (((x ** 2 - 11 * x + 28) > 0) or ((y ** 2 - 9 * y + 14) > 0) or ((x ** 2 + y ** 2) > A)):
            cool = False
            break

    if cool == True:
        print(A)
        break
    