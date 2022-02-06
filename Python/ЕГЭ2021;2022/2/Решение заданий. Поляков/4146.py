from itertools import product


print('№ 4146 К.Ю.Поляков')
print('>>>>>')
print('a b c d')
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if (a <= b) and (not (b == c)) and (d <= a):
                    print(a, b, c, d)


print('>>>>>')
print('a b c d')
for a, b, c, d in product([0, 1], repeat=4):
    if (a <= b) and (not (b == c)) and (d <= a):
        print(a, b, c, d)
