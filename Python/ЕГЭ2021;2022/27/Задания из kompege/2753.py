f = open('27B.txt')
n = int(f.readline())


queue = []
answer = 0

for _ in range(n):
    x = int(f.readline())

    for i in queue:
        if (x+i) % 8 != 0:
            answer += 1

    queue.append(x)

    if len(queue) > 7:
        queue.pop(0)

print(answer)
