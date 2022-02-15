f = open('27B.txt')
n = int(f.readline())


queue = [int(f.readline()) for _ in range(9)]
trash = [0, 0] # кратное 23, не кратное 23

answer = 0


for _ in range(n-9):
    x = int(f.readline())


    if (queue.pop(0) % 23 == 0):
        trash[0] += 1
    else:
        trash[1] += 1


    if (x % 23 == 0):
        answer += sum(trash)
    else:
        answer += trash[0]
    
    
    queue.append(x)


print(answer)
