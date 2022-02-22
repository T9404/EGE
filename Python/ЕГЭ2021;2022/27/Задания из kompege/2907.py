f = open('27B.txt')
n = int(f.readline())


count_30 = [float('inf')] * 30

answer = float('-inf')
k_2, s = 0, 0


for _ in range(n):
    x = int(f.readline())
    s += x

    if (x > 0) and (x % 2 == 0):
        k_2 += 1 

    if k_2 % 30 == 0:
        answer = max(s, answer)
    
    answer = max(answer, s - count_30[k_2 % 30])

    count_30[k_2%30] = min(count_30[k_2 % 30], s)


print(answer)