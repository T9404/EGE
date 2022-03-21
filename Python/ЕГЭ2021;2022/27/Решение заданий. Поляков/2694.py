f = open('27-34b.txt')
n = int(f.readline())


s = [0]

for _ in range(n):

    para = [int(x) for x in f.readline().split()]

    para_2 = [para[0]+para[1], para[0]+para[2], para[1]+para[2]]

    cmb = [a + b for a in para_2 for b in s]

    s = {x % 6: x for x in sorted(cmb, reverse=True)}.values()


m = min(x for x in s if x % 6 == 0)

print(m)
