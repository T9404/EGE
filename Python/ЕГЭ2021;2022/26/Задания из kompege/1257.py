f = open('1257.txt')
n = int(f.readline())


values = sorted([int(x) for x in f.readlines()])
check = set(values)


k, ans = 0, 0

for i in range(len(values)-1):
    for j in range(i+1, len(values)):
        
        if (values[i] % 2 != values[j] % 2) and ((values[i]+values[j]) in check):
            k += 1
            ans = max(values[i]+values[j], ans)

print(k, ans)
