'''
На числовой прямой даны два отрезка: P = [25; 50], Q = [40; 75]. 
Найдите наименьшую возможную длину отрезка A, при котором формула

(x ∈ Q) → ( ((x ∈ P) ≡ (x ∈ Q)) ∨ (¬(x ∈ P) → (x ∈ A)) )

тождественно истинна, то есть принимает значение 1 при любых x.
'''
# https://prnt.sc/sGNe7pRagW_M


def f(x, a1, a2):
    Q = (x in range(40, 75 + 1))
    P = (x in range(25, 50 + 1))
    A = (a1 <= x <= a2)

    return Q <= ((P == Q) or ((not P) <= A))


mini_a = float('inf')


for a1 in range(1, 130):
    for a2 in range(a1, 130):
        if all(f(x, a1, a2) == 1 for x in range(1, 130)):
            if mini_a > a2 - a1:
                mini_a = a2 - a1
                start = a1
                end = a2


print(mini_a)
print(start, end)

print(' p ∈ [25, 50], q ∈ [40, 75]  ==> Ответ: ', end - 50)
