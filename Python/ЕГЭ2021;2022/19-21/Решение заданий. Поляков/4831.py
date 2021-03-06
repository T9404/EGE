'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. 
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в 
кучу один камень, добавить два камня или увеличить количество камней в куче в три раза. 
При этом нельзя повторять ход, который только что сделал второй игрок. Например, если в 
начале игры в куче 4 камня, Петя может первым ходом получить кучу из 5, 6 или 12 камней. 
Если Петя добавил 1 камень и получил кучу из 5 камней, то следующим ходом Ваня может либо 
добавить 2 камня (и получить 7 камней), либо утроить количество камней в куче (их станет 15). 
Получить 6 камней Ваня не может, так как для этого нужно добавить 1 камень, а такой ход только 
что сделал Петя.
Чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается, когда количество камней в куче становится не менее 140. Победителем 
считается игрок, сделавший последний ход, то есть первым получивший кучу, в которой будет 140 
или больше камней. В начальный момент в куче было S камней, 1 ≤ S ≤ 139.
Ответьте на следующие вопросы:

Вопрос 1. Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом 
ходе Пети Ваня может выиграть своим первым ходом.

Вопрос 2. Определите, минимальное и максимальное значения S, при которых у Пети есть выигрышная 
стратегия, причём одновременно выполняются два условия:
− Петя не может выиграть за один ход;
− Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.

  Вопрос 3. Найдите значение S, при котором одновременно выполняются два условия:
– у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом 
при любой игре Пети;
– у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
# https://prnt.sc/D85DR72xV_1p


from functools import lru_cache


def move(values):
    heap, last = values
    new_values = []

    if last != 1:
        new_values += [(heap + 1, 1)]
    if last != 2:
        new_values += [(heap + 2, 2)]
    if last != 3:
        new_values += [(heap * 3, 3)]

    return new_values


@lru_cache(None)
def f(intermediate):
    heap, last = intermediate

    if heap >= 140:
        return 'CP'
    elif any(f(m) == 'CP' for m in move(intermediate)):
        return 'P1'
    elif all(f(m) == 'P1' for m in move(intermediate)):
        return 'B1'
    elif any(f(m) == 'B1' for m in move(intermediate)):
        return 'P2'
    elif all(f(m) in ['P1', 'P2'] for m in move(intermediate)):
        return 'B2'


ans_19 = [i for i in range(1, 139 + 1) if f((i, -1)) == 'B1']
print(*ans_19)

ans_20 = [i for i in range(1, 139 + 1) if f((i, -1)) == 'P2']
print(min(ans_20), max(ans_20))

ans_21 = [i for i in range(1, 139 + 1) if f((i, -1)) == 'B2']
print(*ans_21)
