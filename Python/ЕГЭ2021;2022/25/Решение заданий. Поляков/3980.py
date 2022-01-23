a=[]
for m in range(1,300,2):
    for n in range(0,300,2):
        if 100_000_000<=2**m*5**n<=300_000_000:
            a.append([2**m*5**n,m+n])
a.sort()
for x,y in a:
    print(x,y)
