'''
Имеется набор данных, состоящий из пар положительных целых чисел. Необходимо выбрать из каждой пары ровно одно число так, 
чтобы сумма всех выбранных чисел в шестнадцатеричной системе счисления оканчивалась на F и при этом была минимально возможной.
Гарантируется, что искомую сумму получить можно. Программа должна напечатать одно число – минимально возможную сумму, соответствующую условиям задачи.
'''


f = open('27-26a.txt')
n = int(f.readline())

s = [0]

for _ in range(n):
    para = [int(x) for x in f.readline().split()]

    cmb = [a + b for a in s for b in para]

    s = {x%16:x for x in sorted(cmb, reverse=True)}.values()

m = min(x for x in s if x % 16 == 15)
print(m)
