f=open('C:\\Users\\XiaoMai\\Downloads\\27-92b.txt')
n=int(f.readline())

s=[float('inf')]*n
sum,count_os=0,0
max_sum=0
for _ in range(n):
    x=int(f.readline())
    sum+=x
    if (x>0) and (x%2==0): count_os+=1
    if count_os==1: max_sum=max(max_sum,sum)
    if count_os>1: max_sum=max(max_sum,sum-s[count_os-1])

    s[count_os]=min(s[count_os],sum)

print(max_sum)
