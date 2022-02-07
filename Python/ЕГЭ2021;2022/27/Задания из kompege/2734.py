f = open('27B.txt')
n = int(f.readline())


all_s = [0]*100_000


for _ in range(n):
    x = int(f.readline())
    num = sum(map(int, str(x)))

    all_s[num] += 1


print(max(all_s))
