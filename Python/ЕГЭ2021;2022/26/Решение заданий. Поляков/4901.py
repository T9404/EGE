f=open('C:\\Users\\XiaoMai\\Downloads\\26-72.txt')
s2,s1,n=map(int,f.readline().split())

a=set()
for _ in range(n):
    x1,x2=map(int,f.readline().split())
    a.add((x1,x2))


count=0
min_r=0
max_c=0

for x1 in range(1,s1+1):
    c1=0
    for x2 in range(1,s2+1):
        if (not (x1,x2) in a) and (x2<=s2-3):
            p=[(x1,x) for x in range(x2,x2+4)]
            if all(not x in a for x in p):
                c1+=1
    count+=c1
    if c1>max_c:
        max_c=c1
        min_r=x1

print(count,min_r)

