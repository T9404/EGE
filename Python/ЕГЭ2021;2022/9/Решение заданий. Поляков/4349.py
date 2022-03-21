from itertools import permutations


f = open('9-130.csv')


k = 0

for _ in range(5000):
    a, b, c = map(int, f.readline().split(';'))
    
    for i in permutations([a, b, c], r=3):
        if i[1]-i[0] == i[2]-i[1] and (i[1] - i[0]) != 0:
            k += 1
            break

print(k)
