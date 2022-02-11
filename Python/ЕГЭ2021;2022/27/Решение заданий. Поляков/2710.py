f=open('C:\\Users\\XiaoMai\\Downloads\\27-35b.txt')
n=int(f.readline())

c=0
a=[]
c0=0
for _ in range(n):
    x=int(f.readline())
    if (x==0): c0+=1
    else:
        if (c0>0):
            for q in a:
                if ((q[1]-c0)!=0) and ((q[0]+x)%2==0):
                    c+=1
        a.append([x,c0])

print(c)