f=open('C:\\Users\\XiaoMai\\Downloads\\27-79b.txt')
n=int(f.readline())

d={}

l=0
ma_l=0
for _ in range(n):
    x=int(f.readline())
    l+=1
    if x*x in d:
        ma_l=max(ma_l,l-d[x*x]+1)

    if (x%21==0) and (not x in d): d[x]=l

print(ma_l)







