from itertools import product


d = ['']

for r in range(1, 6+1):
    d += [''.join(sorted(i))
          for i in product('0123456789', repeat=r) if len(set(i)) == len(i)]

arr = set()


for i in d:
    if all(int(i[f]) in [2, 3, 4] for f in range(len(i))):
        for j in d:
            if all(int(j[f]) in [6, 7, 8] for f in range(len(j))):
                x = int('1' + i + '5' + j + '9')
                if x % 21 == 0:
                    arr.add((x, x//21))


for i in sorted(arr, key=lambda u: u[0]):
    print(*i)
