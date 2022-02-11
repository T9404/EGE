f = open('17-243.txt')

a = [int(x) for x in f.readlines()]


cond = ([i for i in a if (i % 61 == 0)])
numb_61 = 0

for i in cond:
    numb_61 += sum(map(int, str(i)))


minn, k = float('inf'), 0

for i in range(len(a)-1):
    d = sorted([a[i], a[i+1]])
    if (d[1] > numb_61 and d[0] <= numb_61) and (d[0] % 100 == 33):
        k += 1
        minn = min(a[i]+a[i+1], minn)

print(k, minn)
