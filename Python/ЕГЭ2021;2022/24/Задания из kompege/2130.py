f=open('C:\\Users\\XiaoMai\\Downloads\\24.txt')
s=str(f.readline())

maxc=0
for i in range(0,len(s)-1):
    if (int(s[i:i+2])<=23) and (int(s[i+2:i+4])<=59):
        k=i+4
        c=1
        while ((int(s[k:k+2])<=23) and (int(s[k+2:k+4])<=59)):
            c+=1
            k+=4
        else: maxc=max(maxc,c)

print(maxc)