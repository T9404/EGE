f = open('27B.txt')
n = int(f.readline())


capture = [int(f.readline()) for _ in range(10)]
mini = float('inf')


for _ in range(n-10):
    x = int(f.readline())

    for y in range(10):
        sumx = x + capture[y]

        if (sumx % 2 == 0) and (sumx % 1071 == 0):
            mini = min(mini, sumx)

    capture.append(x)
    capture.pop(0)

print(mini)
