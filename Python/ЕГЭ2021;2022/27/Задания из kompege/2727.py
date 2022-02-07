f = open('27B.txt')
n = int(f.readline())


k_31 = []
k_other = []


for _ in range(n):
    x = int(f.readline())

    if x % 31 == 0:
        k_31.append(x)
    else:
        k_other.append(x)


print(min(k_31) * min(k_other))
