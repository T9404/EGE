f = open('17-257.txt')
a = [ int(x) for x in f.readlines() ]

nechet = max(i for i in a if (i % 2 != 0))
k = 0
minn = float('inf')

for i in range(len(a)-1):
    if ( 2 * ( a[i] + a[i+1] )) > nechet:
        k += 1
        minn = min(a[i]+a[i+1], minn)

print(k, minn)
