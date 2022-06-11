'''
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит набор карт. 
За один ход игрок берёт одну из карт и кладёт её в стопку поверх предыдущей. 
Игроки ходят по очереди, первую карту кладёт Петя. Первая карта может быть любой 
из доступных. В следующие ходы игроки могут положить только карты того же достоинства 
или на единицу старше. Игра завершается в тот момент, когда положить новую карту в стопку 
становится невозможно. Победителем считается игрок, сделавший последний ход, то есть 
положивший последнюю карту в стопку.
Ответьте на следующие вопросы:

Вопрос 1. Перед игроками лежат 1 семёрка, 3 восьмёрки и 2 девятки. С какой карты Петя 
должен начать игру, чтобы гарантированно выиграть? В качестве ответа запишите числовое 
значение этой карты.

Вопрос 2. Перед игроками лежат 1 пятёрка, 2 шестёрки, 3 семёрки, 1 восьмёрка, 3 девятки, 
2 десятки. С каких карт Петя должен начать игру, чтобы гарантированно выиграть? 
В качестве ответа запишите наименьшее и наибольшее числовые значения этих карт.

Вопрос 3. Известно, что в начальном наборе были четвёрки, пятёрки, шестёрки и семёрки, 
но не более четырёх каждого вида. Сколько существует вариантов наборов таких карт, 
что Ваня сможет победить при любой игре Пети?
'''
# https://prnt.sc/smsy9-6JikZF


from functools import lru_cache
from itertools import product


def move(e):
    # h - список карт, l - последняя карта противника,
    # s - начальная карта всей партии,
    # flag - самая первая карта битвы? тогда мы должны убрать именно её

    h, l, s, flag = sorted(e[:-3]), e[-3], e[-2], e[-1]
    new_step = []

    if flag:
        # убираем карту s, с которой начинаем битву
        intermediate = tuple(h[h.index(s)+1:])
        new_step.append((*intermediate, l, s, False))

    else:
        # значение карт может повторяться. обходим дубликаты
        uniq_cards = set()

        for i in range(len(h)):
            # выбираем карту, которая подходит под условие
            if ((l+1 == h[i]) or (l == h[i])) and (h[i] not in uniq_cards):
                # обрезаем карту и всё до неё
                intermediate = tuple(h[h.index(h[i])+1:])
                # сохраняем использованную карту
                uniq_cards.add(h[i])
                new_step.append((*intermediate, h[i], s, flag))

    return new_step


@lru_cache(None)
def f(h):

    # много карт, много условий
    new = lambda *values: (f(m) in values for m in move(h))

    # список карт пуст, остались l, s, flag =>
    if len(h) == 3:
        return 'W'

    elif any(new('W')):
        return 'P1'
    elif all(new('P1')):
        return 'V1'
    elif any(new('V1')):
        return 'P2'
    elif all(new('P1', 'P2')):
        return 'V2'
    elif any(new('V2')):
        return 'P3'
    elif all(new('P1', 'P2', 'P3')):
        return 'V3'
    elif any(new('V3')):
        return 'P4'
    elif all(new('P1', 'P2', 'P3', 'P4')):
        return 'V4'
    elif any(new('V4')):
        return 'P5'
    elif all(new('P1', 'P2', 'P3', 'P4', 'P5')):
        return 'V5'
    elif any(new('V5')):
        return 'P6'
    elif all(new('P1', 'P2', 'P3', 'P4', 'P5', 'P6')):
        return 'V6'
    elif any(new('V6')):
        return 'P7'
    elif all(new('P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7')):
        return 'V7'
    elif any(new('V7')):
        return 'P8'
    elif all(new('P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8')):
        return 'V8'


cards_19 = (7, 8, 8, 8, 9, 9)

arr19 = [i for i in set(cards_19) if f((*cards_19, i, i, True))[0] == 'P']
print(*arr19)


cards_20 = (5, 6, 6, 7, 7, 7, 8, 9, 9, 9, 10, 10)

arr20 = [i for i in set(cards_20) if f((*cards_20, i, i, True))[0] == 'P']
print(min(arr20), max(arr20))


cards_21 = [[i]*4 for i in range(4, 7+1)]
answer_21 = 0

for i, j, m, u in product(range(4), repeat=4):

    query = tuple(cards_21[0][:i+1] + cards_21[1][:j+1] +
              cards_21[2][:m+1] + cards_21[3][:u+1])

    if len(set(query)) == 4 and all(f((*query, i, i, True))[0] == 'V' for i in range(4, 7+1)):
        answer_21 += 1

print(answer_21)
