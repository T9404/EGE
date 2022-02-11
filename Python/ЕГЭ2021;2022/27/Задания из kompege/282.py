f = open('27-B.txt')
n = int(f.readline())


d = [int(f.readline()) for i in range(8)]
answer = 0

for _ in range(n-8):
    x = int(f.readline())

    h = 0
    
    while len(d) - h >= 8:
        answer = max(x*d[h], answer)
        h += 1

    d.append(x)
    d[0] = max(d[0], d[1])
    d.remove(d[1])


print(answer)
