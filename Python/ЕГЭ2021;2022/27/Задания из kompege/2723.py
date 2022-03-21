f = open('27B.txt')
n = int(f.readline())


k_19 = 0

for _ in range(n):
    x = int(f.readline())

    if x % 19 == 0:
        k_19 += 1

print(k_19 * (k_19-1)//2 * (k_19-2)//3)
