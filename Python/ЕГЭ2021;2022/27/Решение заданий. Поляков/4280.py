f=open('C:\\Users\\XiaoMai\\Downloads\\27-74b.txt')
n=int(f.readline())

count=0
mas=[[0,0]]
for _ in range(n-1):
    x=int(f.readline())
    mas=[[x+b,c+1] for b,c in mas]+[[x,1]]
    num=-1
    for i in mas:
        num+=1
        if (i[0]%39==0) and (i[1]<=20):
            count+=1
        if (i[1]>20):
            mas.remove(i)
print(count)
