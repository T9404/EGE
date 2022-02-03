f = open('27-66b.txt')
n = int(f.readline())


def get():
    return list(map(int, f.readline().split()))


s = [0]

smax = 0

for i in range(n):  

    pair = [x for x in get()]
    # считываем сумму всех чисел для того чтобы сразу найти вторую сумму
    smax += sum(pair)

    cmb = [a+b for a in s for b in pair]
    s = {x % 5: x for x in sorted(cmb)}.values()


m = max(x for x in s if (smax - x) % 3 != 0 and x % 5 != 0)

print(m)
