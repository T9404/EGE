f = open('_')
n = int(f.readline())


max_sum, min_raznica = 0, float('inf')

cet, necet = 0, 0

cet1, necet1 = 0, 0


for _ in range(n):
    a = [int(x) for x in f.readline().split()]
    max_sum += max(a)

    if (max(a) % 2 == 0):
        cet += 1
    else:
        necet += 1

    if ((a[0] % 2) != (a[1] % 2)) and (abs(a[0]-a[1]) < min_raznica):
        min_raznica = abs(a[0]-a[1])

        if (min(a) % 2 == 0):
            cet1 = 1
            necet1 = 0
        else:
            cet1 = 0
            necet1 = 1


if (cet > necet) and (max_sum % 2 == 1) and (cet+cet1 > necet+necet1):
    print(max_sum-min_raznica)
    
if (cet < necet) and (max_sum % 2 == 0) and (cet+cet1 < necet+necet1):
    print(max_sum-min_raznica)
