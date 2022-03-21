f = open('9-127.csv')


k = 0

for _ in range(5000):
    a, b, c = map(int, f.readline().split(';'))
    if b**2 - 4 * a * c < 0:
        k += 1

print(k)
