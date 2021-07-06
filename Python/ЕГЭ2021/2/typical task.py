# В данном задании нет ничего сложного, нужно лишь переписать формулу :)
print('№ 4146 К.Ю.Поляков')
print('>>>>>')
print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (a <= b) and (not (b == c)) and (d <= a):
                    print(a, b, c, d)
print('Вам осталось сопоставить таблицу истинности')

# Короткий способ:

from itertools import product
# см. '../ЕГЭ2021/itertools/learn'

print('>>>>>')
print('a b c d')
for a, b, c, d in product([0, 1], repeat=4):
    if (a <= b) and (not (b == c)) and (d <= a):
        print(a, b, c, d)
