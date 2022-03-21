f = open('2652.txt')  
n = int(f.readline())

barcode = {}

for _ in range(n):
    x = f.readline().strip()

    if x in barcode:
        barcode[x] += 1
    else:
        barcode[x] = 1


mak = 0

for m in barcode.items():
    if m[1] > mak:
        mak = m[1]

print(len(barcode), mak)
