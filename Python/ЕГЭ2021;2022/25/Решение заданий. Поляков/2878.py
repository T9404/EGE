p = []

for k in range(33333, 55556):
    n = str(k)
    
    if all(int(i) % 2 == 0 for i in [n[2], n[4]]) and all(int(i) % 2 == 1 for i in [n[0], n[1], n[3]]) and all(k % i != 0 for i in [6, 7, 8]):
        p.append(k)

print(len(p), max(p)-min(p))
