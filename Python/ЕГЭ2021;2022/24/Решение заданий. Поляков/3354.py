f=open('C:\\Users\\XiaoMai\\Downloads\\24-4.txt')
s=str(f.readline())

l=s[0]
m=''
for i in range(len(s)-1):
  if (s[i]>s[i+1]):
    l+=s[i+1]
    if (len(m)<len(l)):
      m=l
  else:
    l=s[i+1]

print(m)
