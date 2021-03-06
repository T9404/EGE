'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. 
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может

а) добавить в кучу один камень;
б) добавить в кучу два камня;
в) добавить в кучу три камня.

Игра завершается в тот момент, когда количество камней в куче превышает 20. 
Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу, 
в которой будет 21 или больше камней. В начальный момент в куче было S камней, 1 ≤ S ≤ 20.

Задание 19
Известно, что Ваня может гарантированно выиграть своим первым ходом. 
Укажите значение S, с которого началась игра..

Задание 20.
Для игры, описанной в предыдущем задании, укажите три значения S, при которых у Пети есть 
выигрышная стратегия, причём Петя может выиграть своим третьим ходом, независимо от того, 
как будет ходить Ваня. В ответе запишите полученные значения в порядке возрастания.

Задание 21.
Для игры, описанной в задании 19, найдите количество значений S, при котором у Вани есть 
выигрышная стратегия, позволяющая ему выиграть при любой игре Пети.
'''
# https://prnt.sc/R0RB68WyJTBv


def f(a, c, m):
    if a > 20:
        return c % 2 == m % 2
    if c == m:
        return 0

    h = [f(a + 1, c + 1, m), f(a + 2, c + 1, m), f(a + 3, c + 1, m)]

    return any(h) if ((c + 1) % 2 == m % 2) else all(h)


t19, t20, t21 = [], [], set()


for a in range(1, 21):
    for m in range(1, 15):
        if f(a, 0, m) == 1:
            if m == 2:
                t19.append(a)
            if m == 5:
                t20.append(a)
            if m % 2 == 0:
                t21.add(a)


print(min(t19))

print(t20[0], t20[1], t20[2])

print(len(t21))
