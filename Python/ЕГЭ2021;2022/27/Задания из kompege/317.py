f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (1).txt')
n=int(f.readline())

a=[]
c=0
for _ in range(n):
    x=int(f.readline())
    if (x<34):
        for y in a:
            if (y>x) and (y+x<=34):
                c+=1
        a.append(x)

print(c)

