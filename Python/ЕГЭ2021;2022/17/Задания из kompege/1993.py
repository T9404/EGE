f = open('17.txt')
a = [int(x) for x in f.readlines()]
k = 0
mak = float('-inf')

for i in range(len(a)-1):
    sum = abs(a[i]+a[i+1])
    mult = abs(a[i]*a[i+1])
    if sum % 3 == 0 and sum % 6 != 0:
        if mult % 10 == 8:
            k += 1
            mak = max(a[i]+a[i+1], mak)
            
print(k, mak)
