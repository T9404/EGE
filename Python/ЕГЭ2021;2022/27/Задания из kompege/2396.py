f=open('C:\\Users\\XiaoMai\\Downloads\\27_B (5).txt')
n=int(f.readline())

max_sum=0
min_len=float('inf')

p_sum=[10**6]*16
p_len=[10**6]*16

len=0
sum=0
for _ in range(n):
    x=int(f.readline())
    len+=1
    if x%2==0: sum+=x

    if (sum%16==0) and ((sum>max_sum) or((sum==max_sum) and (len<min_len))):
        max_sum,min_len=sum,len

    if (p_sum[sum%16]!=10**6):
        sum1=sum-p_sum[sum%16]
        if (sum1>max_sum) or ((sum1==max_sum) and (len-p_len[sum%16]<min_len)):
           max_sum,min_len=sum1,len-p_len[sum%16]

    if (sum<p_sum[sum%16]) or ((sum==p_sum[sum%16]) and (len<p_len[sum%16])):
        p_sum[sum%16]=sum
        p_len[sum%16]=len

print(min_len)

