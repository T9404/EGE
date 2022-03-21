f = open('C:\\Users\\XiaoMai\\Downloads\\24-j6.txt')
s = str(f.readline())


c, a = 0, 1

for i in range(len(s)-1):
    if (int(s[i]) < int(s[i+1])):
        a += 1
        
        if (a == 5) and (s[i+2] <= s[i+1]):
            c += 1
            a = 1
    else:
        a = 1

print(c)
