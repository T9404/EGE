f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (6).txt')
n=int(f.readline())


a=[]
c,c1=0,0
for _ in range(n):
    x=int(f.readline())
    if (x==1): c1+=1
    if (x!=1) and (x%2==0):
        for i in a:
            if (i[0]%2==0) and ((c1-i[1])%2==0) and ((c1-i[1])>1):
                c+=1
        a.append([x,c1])

print(c)









