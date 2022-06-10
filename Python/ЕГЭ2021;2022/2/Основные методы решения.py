# Внимательно расставьте скобки!

'''
Что нужно знать?
and - ∧
or - v
→ - <=  P.S. подумайте почему
= - ==
≠ - !=


https://letpy.com/handbook/operator-priorities/

Приоритеты логических операций:
1 (выражение в скобках)
2 (отрицание)
3 (умножение)
4 (сложение)
5 (импликация)
6 (равенство)
'''


from itertools import product


# Длинный способ
print('a b c d')

for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (a <= b) and (not (b == c)) and (d <= a):
                    print(a, b, c, d)

print('Вам осталось сопоставить таблицу истинности')




# Короткий способ:
# см. '../ЕГЭ2021/itertools/learn'

for a, b, c, d in product([0, 1], repeat=4):
    if (a <= b) and (not (b == c)) and (d <= a):
        print(a, b, c, d)
