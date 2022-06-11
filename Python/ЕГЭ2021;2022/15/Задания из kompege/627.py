'''
Для какого наименьшего целого числа А выражение

(x ∙ y > A) ∧ (x > y) ∧ (x < 8)

тождественно ложно, т.е. принимает значение 0 при любых целых положительных x и y? 
'''
# https://prnt.sc/xuZgTd7e1FNy


from itertools import product


def f(x, y, a):
    return (x * y > a) and (x > y) and (x < 8)


for a in range(1, 1000):
    ok = 0
    for x, y in product(range(1, 100), repeat=2):
        if f(x, y, a) == 1:
            ok = 1
            break

    if not ok:
        print(a)
        break
