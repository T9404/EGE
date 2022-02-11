# 1 Решение

minc = float('inf')

for k in range(1, 100):
    a = bin(k)[2:]

    for i in range(1, len(a)):
        if (a[i] == '0'):
            a = a.replace('0', '1', 1)
        if (a[i] == '1'):
            a = a.replace('1', '0', 1)
            
    a = int(a, 2)

    if (k+a > 99) and (k % 2 == 1):
        minc = min(minc, k)

print(minc)


# 2 Решение
def f(n):
    n_2 = bin(n)[2:]
    up_n = ''

    for i in range(1, len(n_2)):
        if n_2[i] == '1':
            up_n += '0'
        else:
            up_n += '1'

    n_10 = int(up_n, 2)

    return n+n_10


for x in range(3, 1000, 2):
    if f(x) > 99:
        print(x)
        break
