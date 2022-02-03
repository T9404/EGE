f = open('27-47b.txt')
n = int(f.readline())


s = [0]
max_sum = 0

for _ in range(n):

    para = [int(x) for x in f.readline().split()]
    max_sum += max(para)
    cmb = [a+b for a in s for b in para]
    s = {x % 10: x for x in sorted(cmb, reverse=True)}.values()


x = max(i for i in s if ((max_sum % 10) == (i % 10)))

print(x)
