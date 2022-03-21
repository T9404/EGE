f = open('27B.txt')
n = int(f.readline())


all_s = [0]*10


for _ in range(n):
    x = int(f.readline())

    all_s[int(str(x)[0])] += 1


print(min(i for i in all_s if (i != 0)))
