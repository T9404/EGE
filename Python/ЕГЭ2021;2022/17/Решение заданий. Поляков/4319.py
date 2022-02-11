f = open('17-4.txt')
a = [int(x) for x in f]
k = 0
mik = float('inf')
mak = float('-inf')

def f(x):
    k = 0
    d = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            d.append(i)
            d.append(x//i)
    condition = [i for i in d if (i in [2, 3, 5, 7])]
    if len(condition) == 2:
        return 1
    return 0

for i in range(len(a)): 
    if f(a[i]) and a[i] != 0: 
        k+=1
        mik = min(mik, a[i])
        mak = max(mak, a[i])

print(k, mik+mak)
