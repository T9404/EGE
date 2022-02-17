f = open('27B.txt')
n = int(f.readline())


queue = [int(f.readline()) for _ in range(5)]
ost = [[0, 0] for _ in range(13)]

answer = 0

for _ in range(n-5):
    x = int(f.readline())

    if x % 2 == 0:
        answer += sum(ost[x % 13])
    else:
        answer += ost[x % 13][0]

    ost[queue[0] % 13][queue[0] % 2] += 1


    queue.append(x)
    queue.pop(0)


print(answer)
