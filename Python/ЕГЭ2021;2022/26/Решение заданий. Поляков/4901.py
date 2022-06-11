'''
Игра «Заполни поле» заключается в том, чтобы заполнить прямоугольное поле, разбитое на квадраты. 
Игрок хочет написать программу, которая определила бы сколько есть позиций, в которые можно 
поместить горизонтальные блоки из четырех квадратов.
'''
# https://prnt.sc/7uPiWEwl7ZZJ


f = open('26.txt')
s2, s1, n = map(int, f.readline().split())


nums_pairs = set()
for _ in range(n):
    x1, x2 = map(int, f.readline().split())
    nums_pairs.add((x1, x2))


count, min_r, max_c = 0, 0, 0


for x1 in range(1, s1 + 1):
    amount = 0
    for x2 in range(1, s2 + 1):

        if (not (x1, x2) in nums_pairs) and (x2 <= s2 - 3):
            p = [(x1, x) for x in range(x2, x2 + 4)]
            if all(not x in nums_pairs for x in p):
                amount += 1

    count += amount
    if amount > max_c:
        max_c = amount
        min_r = x1


print(count, min_r)
