f = open('27-94b.txt')
n = int(f.readline())


lens = [float('inf')] * n
defirent = [None]*n

max_len, k5, k7 = 0, 0, 0


for i in range(1, n+1):
    x = int(f.readline())

    if x % 5 == 0:
        k5 += 1
    if x % 7 == 0:
        k7 += 1

        
    if k5 == k7:
        max_len = i

    else:
        if defirent[k5 - k7] != None:
            variant = i - lens[k5-k7]
            max_len = max(variant, max_len)

            
    if i < lens[k5-k7]:
        lens[k5-k7] = i
        defirent[k5 - k7] = k5-k7


print(max_len)
