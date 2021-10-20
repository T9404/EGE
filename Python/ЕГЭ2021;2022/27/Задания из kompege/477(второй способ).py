f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (10).txt')
n=int(f.readline())

count=0
count_chet,count_nechet,min_chet,min_nechet=0,0,float('inf'),float('inf')
for _ in range(n):
    x=int(f.readline())
    if (x%2==0):
        if (x>min_nechet): count+=count_nechet
        count_chet+=1
        min_chet=min(min_chet,x)
    else:
        if (x>min_chet): count+=count_chet
        count_nechet+=1
        min_nechet=min(min_nechet,x)


print(count)

