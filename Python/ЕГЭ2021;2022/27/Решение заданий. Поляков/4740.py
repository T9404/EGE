f=open('C:\\Users\\XiaoMai\\Downloads\\27-88b.txt')
a=[int(x) for x in f.readline().split()]
n=a[0]; k=a[1]

def F(n):
    n=abs(n)
    for i in range(2,int(n**0.5)+1):
        if (n%i==0): return False
    else: return True

s=[float('inf')]*k
m=0
sum=0
c=0
for _ in range(n):
    x=int(f.readline())
    sum+=x
    if (x<0) and (F(x)==True): c+=1

    if (c%k==0): m=max(m,sum)
    m=max(m,sum-s[c%k])

    s[c%k]=min(s[c%k],sum)

print(m)





