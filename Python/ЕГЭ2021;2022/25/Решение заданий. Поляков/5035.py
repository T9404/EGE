from itertools import product


a = []


for i, j, m, n, k in product('012', repeat=5):
    x = '2' + i + '1' + j + '2' + m + '1' + n + '2' + k + '1'
    
    if int(x, 3) % 148 == 0:
        a.append(int(x, 3))


for i in sorted(a, reverse=True):
    print(i, i//148)
