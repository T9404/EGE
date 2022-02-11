f = open('26-k3.txt')
n, gold, bron = map(int, f.readline().split())

a = sorted([int(f.readline()) for x in range(n)])

print(a[-(bron+gold)], end = ' ')
print(a[-gold])
