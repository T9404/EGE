f = open('27B.txt')
n = int(f.readline())


queue = [int(f.readline()) for _ in range(4)]


min_ost = [float('inf')] * 137
max_ost = [0] * 137
ans = 0


for _ in range(n-4):
    x = int(f.readline())


    if min_ost[x % 137] != float('inf'):
        ans = max(ans, abs(min_ost[x % 137] - x))
    
    if max_ost[x % 137] != 0:
        ans = max(ans, abs(max_ost[x % 137] - x))
    

    max_ost[ queue[0] % 137] = max(max_ost[queue[0] % 137], queue[0])
    min_ost[queue[0] % 137] = min(min_ost[queue[0] % 137], queue[0])

    
    queue.append(x)
    queue.pop(0)


print(ans)
   