f=open('C:\\Users\\XiaoMai\\Downloads\\27-B (9).txt')
n=int(f.readline())

max_s,sr_s,min_s=0,0,0
minr=1000000000
for _ in range(n):
    c=[int(x) for x in f.readline().split()]
    maxc,src,minc=max(c),sum(c)-max(c)-min(c),min(c)
    max_s+=maxc
    sr_s+=src
    min_s+=minc
    if (src%2!=minc%2):
        if (maxc!=src):minr=min(minr,maxc-src)
        if (maxc!=minc): minr=min(minr,maxc-minc)

print(max_s-minr)