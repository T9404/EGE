#kompege 27 #1067 Джобс 15.03.2021
f=open('C:\\Users\\XiaoMai\\Downloads\\27-A.txt')
n=int(f.readline())

razn=[]
c1,chet1,c2,chet2 = 0,0,0,0

for _ in range(n):
    a=[int(x) for x in f.readline().split()]
    c1+=max(a)
    if (max(a)%2==0): chet1+=1
    c2+=min(a)
    if (min(a)%2==0): chet2+=1

    if (min(a)%2==0) and (max(a)%2==1):
        razn.append(max(a)-min(a))
razn.sort()
k=0
for a in range((chet1+chet2)//2-chet1):
    k+=razn[a]
print(c1-k)

