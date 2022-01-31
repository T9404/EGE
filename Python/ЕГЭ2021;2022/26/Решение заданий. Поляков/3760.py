f=open('C:\\Users\\XiaoMai\\Downloads\\26-44.txt')
n=int(f.readline())
a=[int(f.readline()) for _ in range(n)]
a.sort()


su=0
max_t=0

mi=1
ma=500
while (ma<=max(a)+1000):
    k=[x for x in a if (mi<=x<=ma)]
    if (len(k)>1):
            su+=0.5*(sum(k[0:len(k)//2]))
            max_t=max(max_t,k[len(k)//2-1]*0.5)
    mi+=500
    ma+=500

print(int(su),int(max_t))


