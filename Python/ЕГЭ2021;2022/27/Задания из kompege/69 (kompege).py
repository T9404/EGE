f=open('C:\\Users\\XiaoMai\\Downloads\\27-B.txt')
n=int(f.readline())

c=0
ost_c=[0]*13
ost_n=[0]*13
for _ in range(n):
    x=int(f.readline())
    ost=x%13
    if (x%2==0):
        c+=ost_c[ost]
        c+=ost_n[ost]
    else: c+=ost_c[ost]

    if (x%2==0): ost_c[ost]+=1
    else: ost_n[ost]+=1

print(c)


