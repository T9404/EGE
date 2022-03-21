f = open('27B.txt')
n = int(f.readline())


chet = []
nechet = []


for _ in range(n):
    x = int(f.readline())

    if x % 2 == 0:
        chet.append(x)
    else:
        nechet.append(x)


chet.sort(reverse=True)
nechet.sort(reverse=True)

pick = chet[:2] + nechet[:2]  # выборка


mak = 0

for i in range(len(pick)-1):
    for j in range(i+1, len(pick)):
        if (pick[i]+pick[j]) % 2 != 0:
            mak = max(mak, pick[i]+pick[j])

print(mak)
