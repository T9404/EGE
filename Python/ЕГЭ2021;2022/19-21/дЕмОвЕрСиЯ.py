#  Подробное объяснение автора
# https://www.youtube.com/watch?v=-cD14dribi4&t=8771s&ab_channel=AlexDanov


def f(s):
    return s+1,  s*2


def win(s):
    return s >= 29


# все значения кучи
z = {s for s in range(1, 29)}


# если попадаем в победу, Петя1
p1 = {s for s in z if any(win(t) for t in f(s))}


# вычитаем позиции, чтобы из них не ходить
z -= p1


# всеми ходами попадаем в Петя1, значит Ваня1
v1 = {s for s in z if all(t in p1 for t in f(s))}
print(*sorted(v1))


# не ходим повторно в позиции
z -= v1


# Попадаем в Ваня 1 - мы Петя 2
p2 = {s for s in z if any(t in v1 for t in f(s))}
print(*sorted(p2))


# не ходим повторно в позиции
z -= p2  


# попадаем в p1 или p2 ( " | " )
v2 = {s for s in z if all(t in p1 | p2 for t in f(s))}
print(*sorted(v2))


# не ходим повторно в позиции
z -= v2
