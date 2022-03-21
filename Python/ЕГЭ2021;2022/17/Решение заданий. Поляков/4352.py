f = open('17-5.txt')

a = [int(x) for x in f]


k, sumka = 0, 0

for i in range(1, len(a)):
    if abs(a[i-1]) % 10 == 7 or abs(a[i]) % 10 == 7:
        k += 1
        sumka = max(sumka, a[i-1]+a[i])

print(k, sumka)
