'''
Демоверсия 2022
На числовой прямой даны два отрезка: D = [17; 58] и C = [29; 80]. 
Укажите наименьшую возможную длину такого отрезка A, для которого логическое выражение  

(x ∈ D) → ((¬(x ∈ C) ∧ ¬(x ∈ A)) → ¬(x ∈ D)) 

истинно (т.е. принимает значение 1) при любом значении переменной х. 
'''
# https://prnt.sc/dCeoOpq-wwRQ


D = range(17, 58+1)
C = range(29, 80+1)


def f(x, a1, a2):
    D = (x in set(range(17, 58+1)))
    C = (x in set(range(29, 80+1)))
    A = (a1 <= x <= a2)

    return D <= (((not C) and (not A)) <= (not D))


min_a = float('inf')


for a1 in range(15, 85):
    for a2 in range(a1, 85):
        if all(f(x, a1, a2) == 1 for x in range(-10, 5000)):
            if min_a > (a2 - a1):
                min_a = a2 - a1
                start = a1
                end = a2


print(start, end)
print(min_a)

print('answer: ', 29 - start)
