'''
Для какого наибольшего целого неотрицательного числа А выражение
(2y + x ≠ 70) ∨ (x < y) ∨ (A < x)

тождественно истинно, т.е. принимает значение 1 при любых целых неотрицательных x и y?
'''
# https://prnt.sc/kup4zTrC1u6L


from itertools import product


def f(x, y, a):
    return (2 * y + x != 70) or (x < y) or (a < x)


for a in range(1, 1000):
    if all(f(x, y, a) == 1 for x, y in product(range(0, 100), repeat=2)):
        answer = a

print(answer)
