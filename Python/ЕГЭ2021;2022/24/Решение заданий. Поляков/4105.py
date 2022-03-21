f = open('C:\\Users\\XiaoMai\\Downloads\\24-168 (1).txt')
s = str(f.readline())


m = 0
l = s[0]


for i in range(1, len(s)-1):
    if (s[i-1] <= s[i]):
        l += s[i]
        k = set(l)

        if (len(k)) == 4:
            l = l[0:len(l)-1]
            m = max(m, len(l))
            l = s[i]
    else:
        l = s[i]


print(m)
