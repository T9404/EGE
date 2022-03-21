#  Подробное объяснение автора
# https://www.youtube.com/watch?v=-cD14dribi4&t=8771s&ab_channel=AlexDanov
# Другие реализации смотрите далее

def f(s):  # ходы
    return s+1,  s*2


def win(s):  # определение победы
    return s >= 29


z = {s for s in range(1, 29)}  # все значения кучи

# если попадаем в победу, Петя1
p1 = {s for s in z if any(win(t) for t in f(s))}

z -= p1  # вычитаем позиции, чтобы из них не ходить

# всеми ходами попадаем в Петя1, значит Ваня1
v1 = {s for s in z if all(t in p1 for t in f(s))}
print(*sorted(v1))
z -= v1  # не ходим повторно в позиции

# Попадаем в ВАня1 - мы Петя2
p2 = {s for s in z if any(t in v1 for t in f(s))}
print(*sorted(p2))
z -= p2  # пиу-пам


# попадаем в p1 или p2 ( " | " )
v2 = {s for s in z if all(t in p1 | p2 for t in f(s))}
print(*sorted(v2))
z -= v2
