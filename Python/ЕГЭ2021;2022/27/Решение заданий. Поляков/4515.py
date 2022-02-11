f=open('C:\\Users\\XiaoMai\\Downloads\\27-82b.txt')
n=int(f.readline())

def F(n):
    for i in range(2,int(n**0.5)+1):
        if (n%i==0): return 0
    else: return 1

max_s=c=sum=0
ost=[float('inf')]*9
for _ in range(n):
    x=int(f.readline())
    c+=F(x)
    sum+=x
    if (c%9==0):
        max_s=sum
    else:
        if ost[c%9]!=float('inf'):
            max_s=max(max_s,sum-ost[c%9])
    ost[c%9]=min(ost[c%9],sum)
print(max_s)