f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (2).txt')
n=int(f.readline())

a=[]
c=0
for _ in range(n):
    x=int(f.readline())
    ost=x%2
    q=[d for d in a if (d%2==(1-ost))]
    if (len(q)!=0):
        min_q=min(q)
        if (x>min_q):
            c+=len(q)
    a.append(x)

print(c)



