f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (4).txt')
n=int(f.readline())

a=[]
c=0
for _ in range(n):
    x=int(f.readline())
    for y in a:
        if (y<x) and (y+x>50):
            c+=1
    a.append(x)

print(c)







