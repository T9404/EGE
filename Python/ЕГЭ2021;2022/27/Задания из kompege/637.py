f = open('27-B (1).txt')
n = int(f.readline())

s = [0]

for _ in range(n):
    para = [int(x) for x in f.readline().split() ]
    cmb = [a+b for a in s for b in para]
    s = {x%10:x for x in sorted(cmb)}.values()

answer = max([i for i in s if i % 10 != 5])
print(answer)
