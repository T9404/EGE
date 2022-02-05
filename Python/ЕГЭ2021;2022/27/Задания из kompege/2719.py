f = open('27B.txt')
n = int(f.readline())


value_chet = [0, 0]

k = 0

for _ in range(n):
    x = int(f.readline())

    k += value_chet[x % 2]
    value_chet[x % 2] += 1

print(k)
